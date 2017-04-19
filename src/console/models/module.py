import os
from jsonschema import validate
from math import sin, pi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, orm
from config import (
    LOGGER,
)
Base = declarative_base()

class Module(Base):

    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    hostname = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)


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


    def flash(self):
        print 'flashing module {}'.format()
        threading.thread(target=self.flash_thread, args=(0.0,)).start()

    def __repr__(self):
        return '<Module {} ({}) location: {} numLEDs: {}'.format(self.name,
                                                                 self.MAC,
                                                                 self.location,
                                                                 self.numLEDs)
