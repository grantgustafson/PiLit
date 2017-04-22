class Strobe:

    def __init__(self,
                interval = .25,
                min_i = 0.0,
                max_i = 1.0,
                duty_cycle=.5,
                duration = 4):
        self.interval = interval
        self.min_i = min_i
        self.max_i = max_i
        self.duty_cycle = duty_cycle
        self.last_update = None
        self.start_time = None
        self.duration = duration

    def update(self, time):
        if self.start_time is None:
            self.start_time = time
            self.last_update = time
        else:
            self.last_update = time
        t_delta = self.start_time - time
        if (t_delta % self.interval) < self.interval * self.duty_cycle:
            return [self.max_i] * self.length
        else:
            return [self.min_i] * self.length

    def is_finished(self):
        return self.last_update - self.start_time > self.duration
