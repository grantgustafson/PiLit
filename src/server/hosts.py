import requests
import threading
from config import HOSTS_PATH

URL = 'http://{}.local:8123/status'

class Hosts:

    _shared_state = {}
    _instantiated = False

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._instantiated:
            self._load_hosts()
            self._host_status = {}
            self._is_detecting = False
            self._instantiated = True
        self._detect()

    def _get_status(self, hostname):
        try:
            r = requests.get(URL.format(hostname))
            print '{} online'.format(hostname)
            self._host_status[hostname] = True
        except requests.ConnectionError as ce:
            print '{} not online'.format(hostname)
            self._host_status[hostname] = False

    def _load_hosts(self):
        with open(HOSTS_PATH) as f:
            self._hosts = [x.strip() for x in f.readlines()]
        print self._hosts

    def _detect(self):
        for host in self._hosts:
            threading.Thread(target=self._get_status, args=(host,)).start()
        self._detect_timer()

    def _detect_timer(self):
        print self._host_status
        if self._is_detecting:
            threading.Timer(10, self._detect).start()

    def start_detection(self):
        self._is_detecting = True
        self._detect()

    def stop_detection(self):
        self._is_detecting = False

if __name__ == '__main__':
    hosts = Hosts()
    hosts.start_detection()
