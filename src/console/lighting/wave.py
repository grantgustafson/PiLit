from colorsys import hsv_to_rgb
from math import ceil, floor, cos, pi, sin
from util import calc_c_rate

class Wave:

    def __init__(self, speed=1.0, width=20.0, start_pos=0.0):
        self.speed = speed
        self.width = width
        self.length = 64
        self.pos = start_pos
        self.last_update = None
        self.type = 'intensity'

    def update(self, time):
        if self.last_update:
            t_delta = time - self.last_update
            self.pos += 50*(self.speed * t_delta)
            self.last_update += t_delta
        else:
            self.last_update = time

        intensities = [0] * self.length
        x_1 = int(ceil(self.pos - self.width/2))
        for i in range(int(floor(self.width))):
            x_i = x_1 + i
            if x_i >= 0 and x_i < self.length:
                intensities[x_i]=cos((x_i - self.pos)*pi/self.width)
        return intensities

    def is_finished(self):
        return (self.pos + self.width < 0 and self.speed <= 0) or \
               (self.pos - self.width > self.length  and self.speed >= 0)

class StandingWave:

    def __init__(self,
                 speed=1.0,
                 width=32.0,
                 min_i=0.0,
                 max_i = 1.0,
                 duration = 10.0):
        self.speed = speed
        self.width = width
        self.length = 64
        self.omega = 0.0
        self.min_i = min_i
        self.max_i = max_i
        self.range = max_i - min_i
        self.duration = duration
        self.start_time = None
        self.last_update = None
        self.type = 'intensity'

    def update(self, time):
        if self.last_update:
            self.omega += self.speed * (time - self.last_update)
        else:
            self.start_time = time
        self.last_update = time

        I = [0] * self.length
        for i in range(self.length):
            v = 0.5 + 0.25*sin(2*pi*i/self.width - self.omega) + \
                           0.25*sin(2*pi*i/self.width + self.omega)
            I[i] = v*self.range + self.min_i
        return I


    def is_finished(self):
        return self.last_update - self.start_time > self.duration


class GradientWave:

    def __init__(self,
                 speed=1.0,
                 width=30.0,
                 start_pos=-5.0,
                 c1=0.0,
                 c2=0.6,
                 sat=1.0,
                 min_i = .5,
                 max_i = 1.0,
                 forwards=False):
        self.speed = speed
        self.width = width
        self.length = 64
        self.pos = start_pos
        self.min_i = min_i
        self.range = max_i - min_i
        self.last_update = None
        self.forwards = forwards
        self.c1 = c1
        self.sat = sat
        self.c2 = c2
        self.c_rate = calc_c_rate(c2, c1, width, not forwards)
        self.type = 'combo'

    def update(self, time):
        if self.last_update:
            t_delta = time - self.last_update
            self.pos += 50*(self.speed * t_delta)
            self.last_update += t_delta
        else:
            self.last_update = time

        V = [self.min_i] * self.length
        H = [self.c1] * self.length
        x_1 = int(ceil(self.pos - self.width/2))
        num_pixels = int(floor(self.width))
        for i in range(num_pixels):
            x_i = x_1 + i
            if x_i >= 0 and x_i < self.length:
                V[x_i]=cos((x_i - self.pos)*pi/self.width) * self.range + self.min_i
                H[x_i] = (self.c2 + i * self.c_rate) % 1.0
        for i in range(x_1 + 1):
            if i >= 0 and i < self.length:
                H[i] = self.c2
        return zip(H, [self.sat] * self.length, V)

    def is_finished(self):
        return (self.pos + self.width < 0 and self.speed <= 0) or \
               (self.pos - self.width > self.length  and self.speed >= 0)
