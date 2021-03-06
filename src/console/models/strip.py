from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    orm,
    ForeignKey
    )
from colorsys import hsv_to_rgb
from sqlalchemy.orm import relationship
from config import (
    LOGGER,
    Base
)

class Strip(Base):
    __tablename__ = 'strips'

    id = Column(Integer, primary_key=True)
    length = Column(Integer, nullable=False)
    segments = relationship('Segment', back_populates='strip', lazy='joined')
    name = Column(String(64), nullable=False)

    def __init__(self, length, name):
        self.length = length
        self.name = name
        self._setup()


    @orm.reconstructor
    def _setup(self):
        self.compiled_rgb = [(0,0,0)] * self.length
        self.color_controls = []
        self.intensity_controls = []
        self.combo_controls = []
        self.hsvs = []
        self.last_update = None

    def hsvs_to_rgbs(self, hsv):
        return tuple([x * 255 for x in hsv_to_rgb(hsv[0], hsv[1], hsv[2])])

    def filter_controls(self):
        self.color_controls = filter(lambda c: not c.is_finished(), self.color_controls)
        self.intensity_controls = filter(lambda c: not c.is_finished(), self.intensity_controls)
        self.combo_controls = filter(lambda c: not c.is_finished(), self.combo_controls)
    def compile(self, time):
        if (self.last_update == time):
            return

        if len(self.combo_controls) == 0 and len(self.color_controls) == 0:
            return

        if len(self.combo_controls) > 0:
            for control in self.combo_controls:
                self.hsvs = control.update(time)
                self.compiled_rgb = map(lambda c: self.hsvs_to_rgbs(c), self.hsvs)
            self.filter_controls()
            return

        H = [0.0] * self.length
        S = [0.0] * self.length
        V = [0.0] * self.length
        for control in self.intensity_controls:
            for idx, v in enumerate(control.update(time)):

                 V[idx] += v

        for control in self.color_controls:
            for idx, (h, s) in enumerate(control.update(time)):
                H[idx] += h
                S[idx] += s
        self.filter_controls()
        self.compiled_rgb = map(lambda hsv: self.hsvs_to_rgbs(hsv), zip(H, S, V))


    def add_color_control(self, control, clear=False):
        if clear:
            self.color_controls = []
        self.color_controls.append(control)
        control.length = self.length

    def add_intensity_control(self, control, clear=False):
        if clear:
            self.intensity_controls = []
        self.intensity_controls.append(control)
        control.length = self.length


    def add_combo_control(self, control, clear=False):
        if clear:
            self.combo_controls = []
        self.combo_controls.append(control)
        control.length = self.length

    def set_rgbs(self, rgbs):
        if not len(rgbs) == self.length:
            #TODO throw error
            return
        self.compiled_rgb = rgbs

    def get_rgb(self):
        return self.compiled_rgb

    def __getitem__(self, key):
        return self.compiled_rgb[key]
