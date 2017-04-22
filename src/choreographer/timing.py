import time
from subprocess import Popen, PIPE

TIME_SCRIPT = 'scripts/current_pos.scpt'
DIFF = -0.53

class SpotifyTime:

    _instantiated = False
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._instantiated:
            self._instantiated = True


    def get_player_pos(self):
        start_time = time.time()
        proc = Popen([TIME_SCRIPT], stdout=PIPE, stderr=PIPE)
        pos, _ = proc.communicate()
        return float(pos.strip()) + DIFF
