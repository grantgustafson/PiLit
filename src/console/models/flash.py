import threading
from opc import Client
from math import cos, pi
from config import OPC_PORT

class Flash:

    def __init__(self, hostname):
        self.hostname = hostname
        self.client = Client('{}.local:{}'.format(self.hostname, OPC_PORT))

    def _flash_thread(self, x):
        i = 0.5 * (1.0 + cos(x - pi)) * 255
        pixels = [(i, 0, 0)] * 124
        self.client.put_pixels(pixels)
        x += pi / 60.0
        if x <= 4.0*pi:
            threading.Timer(1/60.0, self._flash_thread, args=(x,)).start()
        else:
            self.client.put_pixels([(0,0,0)]*124)
    def start(self):
        print 'flashing module {}'.format(self.hostname)
        threading.Thread(target=self._flash_thread, args=(0.0,)).start()
