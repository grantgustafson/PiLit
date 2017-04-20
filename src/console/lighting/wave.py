from colorsys import hsv_to_rgb
from math import ceil, floor, cos, pi

class Wave:

    def __init__(self, speed=1.0, width=20.0, start_pos=0.0):
        self.speed = speed
        self.width = width
        self.length = 64
        self.pos = start_pos
        self.last_update = None

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
