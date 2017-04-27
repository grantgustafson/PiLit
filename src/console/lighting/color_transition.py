
from math import ceil, floor, cos, pi
from util import calc_c_rate

class ColorTransition:
    @classmethod
    def get_default():
        return ColorTransition().__dict__

    def __init__(self,
                 h1=.45,
                 h2=.04,
                 forwards=True,
                 duration=10.0
                 ):
        self.length = 64
        self.forwards = forwards
        self.h1 = h1
        self.h2 = h2
        self.duration = duration
        self.type = 'color'
        self.last_update = None

    def start(self):
        self.color = self.h1
        self.end_color = self.h2
        self.c_rate = calc_c_rate(self.h1, self.h2, self.duration, self.forwards)
# d = r*t
# 2pi = r * p

    def update(self, time):
        if self.last_update is not None:
            t_delta = time - self.last_update
            self.color = (self.color + self.c_rate * t_delta) % 1.0
            self.last_update += t_delta
        else:
            self.start()
            self.last_update = time
            self.start_time = time
        if self.last_update - self.start_time > self.duration:
            self.color = self.end_color
        return zip([self.color] * self.length, [1.0] * self.length)

    def is_finished(self):
        return False
