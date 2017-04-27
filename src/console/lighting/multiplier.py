class Multiplier:

    def __init__(self, ctrls):
        self.ctrls = ctrls
        self.started = False

    def update(self, time):
        if not self.started:
            for ctrl in self.ctrls:
                ctrl.length = self.length
        I = [1.0] * self.length

        for update in map(lambda c: c.update(time), self.ctrls):
            for idx, i in enumerate(update):
                I[idx] *= i
        return I
    def is_finished(self):
        return reduce(lambda u1, u2: u1.is_finished and u2.is_finished)
