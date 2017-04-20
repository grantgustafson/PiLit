
from math import ceil, floor, cos, pi

class IntensityWave:

    def __init__(self, min_i=0.0, max_i=1.0, period=2.0, lifetime=10.0):
        self.min = min_i
        self.max = max_i
        self.length = 64
        self.last_update = None
        self.start_time = None
        self.range = max_i - min_i
        self.rate = 2 * pi / period
        self.x = 0.0
        self.lifetime = lifetime
# d = r*t
# 2pi = r * p

    def update(self, time):
        if self.last_update:
            t_delta = time - self.last_update
            self.x += self.rate * t_delta
            self.last_update += t_delta
        else:
            self.last_update = time
            self.start_time = time
        return .5 * (1 + cos(self.x - pi)) * self.range + self.min

    def is_finished(self):
        return self.last_update - self.start_time > self.lifetime
