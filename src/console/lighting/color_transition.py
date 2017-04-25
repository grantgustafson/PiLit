
from math import ceil, floor, cos, pi

class ColorTransition:

    def __init__(self,
                 start_color=.45,
                 end_color=.04,
                 start_sat=1.0,
                 end_sat=1.0,
                 duration=5.0,
                 nextc=[]):
        self.length = 64
        self.last_update = None
        self.start_time = None
        self.color = start_color
        self.end_color = end_color
        self.sat = start_sat
        self.end_sat = end_sat
        self.c_rate = (start_color + end_color) / duration
        self.s_rate = (end_sat - start_sat) / duration
        self.lifetime = duration
        self.nextc = nextc
        self.type = 'color'
# d = r*t
# 2pi = r * p

    def update(self, time):
        if self.last_update:
            t_delta = time - self.last_update
            self.color = (self.color + self.c_rate * t_delta) % 1.0
            self.sat += self.s_rate * t_delta
            self.last_update += t_delta
        else:
            self.last_update = time
            self.start_time = time
        if self.is_finished():
            self.color = self.end_color
            self.sat = self.end_sat
        return zip([self.color] * self.length, [self.sat] * self.length)

    def is_finished(self):
        return self.last_update - self.start_time >= self.lifetime
