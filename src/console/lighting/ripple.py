from math import cos, pi, ceil, floor
class Ripple:

    def __init__(self, speed=1.0, max_i = 1.0, min_i = 0.0, width = 7, center = 20.0):
        self.speed = speed
        self.height = 0.0
        self.max_i = max_i
        self.width = width
        self.min_i = min_i
        self.range = max_i - min_i
        self.center = center
        self.start_time = None
        self.last_update = None
        self.dist = 0.0
        self.type = 'intensity'



    def update(self, time):
        if self.start_time is None:
            self.start_time = time
            self.decay = self.range / min(self.length - self.center, self.center)
        else:
            t_delta = time - self.last_update
            self.dist += t_delta * self.speed * 50
        self.last_update = time

        scalar = min(self.dist, 1.0)
        width = scalar*self.width

        h_dist = max(self.dist - scalar, 0)
        scalar = max(scalar * self.range * (1.0 - self.decay * h_dist), 0.0)
        x_b1 = int(ceil(self.center - (width + h_dist)))
        x_f1 = int(ceil(self.center + h_dist))
        num_in_wave = int(floor(width))

        I = [self.min_i] * self.length

        for i in range(x_b1, x_b1 + num_in_wave):
            if i < 0 or i >= self.length:
                continue
            x = i - self.center + h_dist
            I[i] = .5 * (1.0 + cos(x*pi/width)) * scalar

        for i in range(x_b1 + num_in_wave, x_f1):
            if i < 0 or i >= self.length:
                continue
            I[i] = scalar

        for i in range(x_f1, x_f1 + num_in_wave):
            if i < 0 or i >= self.length:
                continue
            x = i - (self.center + h_dist)
            I[i] = .5 * (1.0 + cos(x*pi/width)) * scalar
        return I
    def is_finished(self):
        return False

if __name__ == "__main__":
    r = Ripple(width = 4, center = 9.3)
    r.length = 20
    print r.update(0)
    print r.update(1)
    print r.update(2)
    print r.update(2.2)
    print r.update(9)
