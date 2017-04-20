from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    orm,
    ForeignKey
    )
from sqlalchemy.orm import relationship
from models.strip import Strip
from config import (
    LOGGER,
    Base
)


class Segment(Base):

    __tablename__ = 'segments'

    id = Column(Integer, primary_key=True)
    num_pixels = Column(Integer, nullable=False)
    module_startpixel = Column(Integer, nullable=False)
    forwards = Column(Boolean, nullable=False)
    strip_startpixel = Column(Integer)
    module_id = Column(Integer, ForeignKey('modules.id'))
    light_module = relationship('LightModule', back_populates='segments', lazy='joined')
    strip_id = Column(Integer, ForeignKey('strips.id'))
    strip = relationship(Strip, back_populates='segments', lazy='joined')

    def __init__(self, num_pixels, module_startpixel=0, forwards=True, **kwargs):
        self.num_pixels = num_pixels
        self.module_startpixel = module_startpixel
        self.forwards = forwards
        for key, val in kwargs.items():
            assert key in self.__table__.columns
            setattr(self, key, val)
        self._setup()

    @orm.reconstructor
    def _setup(self):
        self.direction = 1
        if not self.forwards:
            self.direction = -1

    def render(self, time):
        if self.strip is None:
            return [(0,0,0)] * self.num_pixels
        self.strip.compile(time)
        if self.forwards:
            start = self.strip_startpixel
            end = self.strip_startpixel + self.num_pixels
        else:
            start = self.strip_startpixel + self.num_pixels
            end = self.strip_startpixel - 1
        if end == -1:
            return self.strip.get_rgb()[start : : self.direction]
        else:
            return self.strip.get_rgb()[start : end : self.direction]

        return data
