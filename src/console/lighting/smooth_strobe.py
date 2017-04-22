from math import ceil, floor, cos, pi

class SmoothStrobe:

    def __init__(self,
                interval = .25,
                min_i = 0.0,
                max_i = 1.0,
                duration = 4):
        self.interval = interval
        self.min_i = min_i
        self.max_i = max_i
        self.last_update = None
        self.start_time = None
        self.x = 0.0
        self.rate = 2 * pi / interval
        self.duration = duration
        self.scale = max_i - min_i

    def update(self, time):
        if self.start_time is None:
            self.start_time = time
            self.last_update = time
        else:
            self.x += self.rate * (time - self.last_update)
            self.last_update = time

        v = (1.0 + cos(self.x)) * .5 * self.scale + self.min_i
        return [v] * self.length


    def is_finished(self):
        return self.last_update - self.start_time > self.duration
