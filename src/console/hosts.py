import requests
import threading
from config import HOSTS_PATH
import signal

URL = 'http://{}.local:8123/status'

class Hosts:

    _shared_state = {}
    _instantiated = False

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._instantiated:
            self._load_hosts()
            self.online_hosts = {}
            self._is_detecting = False
            self._instantiated = True
            self.start_detection()

    def get_host_dict(self, name):
        if name in self.online_hosts:
            return {'ip' : self.online_hosts[name],
                    'hostname': name}
        else:
            return None

    def _get_status(self, hostname):
        try:
            r = requests.get(URL.format(hostname))
            data = r.json()
            self.online_hosts[hostname] = data['ip']

        except requests.ConnectionError as ce:
            if hostname == 'testhost':
                self.online_hosts[hostname] = '10.0.0.5'
            elif hostname in self.online_hosts:
                del self.online_hosts[hostname]



    def _load_hosts(self):
        with open(HOSTS_PATH) as f:
            self._hosts = [x.strip() for x in f.readlines()]
        print self._hosts

    def _detect(self):
        for host in self._hosts:
            threading.Thread(target=self._get_status, args=(host,)).start()
        self._detect_timer()

    def _detect_timer(self):
        if self._is_detecting:
            t = threading.Timer(10, self._detect)
            t.setDaemon(True)
            t.start()

    def start_detection(self):
        if not self._is_detecting:
            self._is_detecting = True
            self._detect()

    def stop_detection(self):
        self._is_detecting = False



if __name__ == '__main__':
    hosts = Hosts()
    hosts.start_detection()
