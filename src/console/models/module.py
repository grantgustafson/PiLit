import os
from jsonschema import validate
from math import sin, pi

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, orm
from sqlalchemy.orm import relationship
from segment import Segment
from config import (
    LOGGER,
    Base
)


class LightModule(Base):

    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    name = Column(String(64), nullable=True)
    segments = relationship('Segment', back_populates='light_module', lazy='joined')


    @orm.reconstructor
    def init_instance(self):
        self.ip = None

    def to_dict(self):
        return dict((column.name, getattr(self, column.name))
                for column in self.__table__.columns)

    def to_web_dict(self):
        data = self.to_dict()
        data['ip'] = self.ip
        return data

    def render(self, time):
        data = []
        for segment in self.segments:
            start = segment.module_startpixel
            data += [(0,0,0)] * (start - len(data))
            data += segment.render(time)
        return data

    def __repr__(self):
        return '<Module {} ({}) location: {}'.format(self.name,
                                                     self.hostname,
                                                     self.location)
