import os
from jsonschema import validate
from opc import Client
from math import sin, pi
import threading
from config import (
    LOGGER,
    MODULE_FILE_PATH,
    MODULE_SCHEMA_PATH,
    OPC_PORT,

)

class Light_Module:

    def __init__(self, data, schema, ip=None):
        self.MAC = data['MAC']
        self.name = data['name']
        self.hostname = data['hostname']
        self.location = data['location']
        self.numLEDs = data['numLEDs']
        self.ip = ip
        self.online = False
        self.schema = schema
        self.client = None

    def to_dict(self):
        data = {}
        for key in self.schema['properties']:
            data[key] = getattr(self, key)
        return data

    def to_web_dict(self):
        data = self.to_dict()
        data['ip'] = self.ip
        return data

    def flash_thread(self, x):
        i = cos(x) * 255
        pixels = [(i, 0, 0)] * 124
        self._send_pixels(pixels)
        x += pi / 120.0
        if x <= pi:
            threading.timer(1/60.0, self.flash_thread, args=(x,)).start()

    def flash(self):
        print 'flashing module {}'.format()
        threading.thread(target=self.flash_thread, args=(0.0,)).start()


    def _send_pixels(pixels):
        if not self.client:
            self.client = opc.Client('{}.local:{}'.format(self.hostname, OPC_PORT))
        self.client.put_pixels(pixels)




    def __repr__(self):
        return '<Module {} ({}) location: {} numLEDs: {}'.format(self.name,
                                                                 self.MAC,
                                                                 self.location,
                                                                 self.numLEDs)
