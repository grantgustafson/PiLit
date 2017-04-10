import os
from jsonschema import validate
from config import (
    LOGGER,
    MODULE_FILE_PATH,
    MODULE_SCHEMA_PATH,
)

class Light_Module:

    def __init__(self, data, schema):
        self.MAC = data['MAC']
        self.name = data['name']
        self.location = data['location']
        self.numLEDs = data['numLEDs']
        self.ip = None
        self.online = False
        self.schema = schema

    def to_dict(self):
        data = {}
        for key in self.schema['properties']:
            data[key] = getattr(self, key)
        return data

    def to_web_dict(self):
        data = self.to_dict()
        data['ip'] = self.ip
        return data


    def __repr__(self):
        return '<Module {} ({}) location: {} numLEDs: {}'.format(self.name,
                                                                 self.MAC,
                                                                 self.location,
                                                                 self.numLEDs)
