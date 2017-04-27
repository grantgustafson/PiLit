from hosts import Hosts
import threading
from opc import Client
import time
from config import (
    OPC_PORT
)

REFRESH_RATE = 60
PRINT_RATE = False

class LightEngine:

    def __init__(self, modules, refresh_rate=REFRESH_RATE, debug=False):
        self.hosts = Hosts()
        self.refresh_rate = refresh_rate
        self.debug = debug
        self.modules = [(m, Client('{}.local:{}'.format(m.hostname, OPC_PORT))) for m in modules]
        self.active = True
        self.time_taken = 0.0
        self.i = 0
        self.update()

    def update(self):
        start_time = time.time()
        for module, client in self.modules:
            if module.hostname == 'testhost':
                continue
            if module.hostname in self.hosts.online_hosts:
                client.put_pixels(module.render(start_time))
            if self.debug:
                print module.render(start_time)

        if self.active:
            time_taken = time.time() - start_time
            delay_time = max(1.0/self.refresh_rate - time_taken, 0)
            t = threading.Timer(delay_time, self.update)
            t.setDaemon(True)
            t.start()
            self.i += 1
            self.time_taken += time_taken
            if PRINT_RATE:
                if self.i % self.refresh_rate == 0 :
                    print 'Avg time taken: {}'.format(self.time_taken / self.i)
                    self.i = 0
                    self.time_taken = 0
