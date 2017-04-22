from util import calc_c_rate
class Gradient:

    def __init__(self,
                 c1 = 0.0,
                 c2 = 1.0,
                 end_c1 = None,
                 end_c2 = None,
                 nextc = [],
                 sat = 1.0,
                 x1 = 0,
                 x2 = None,
                 forwards = True,
                 duration = 4.0):
        self.start_c1 = c1
        self.c1 = c1
        self.start_c2 = c2
        self.c2 = c2
        self.sat = sat
        self.end_c1 = end_c1
        self.end_c2 = end_c2
        self.x1 = x1
        self.x2 = x2
        self.forwards = forwards
        self.nextc = []
        self.duration = duration
        self.last_update = None
        self.start_time = None

        self.c1_rate = 0.0
        if self.end_c1:
            self.c1_rate = calc_c_rate(c1, end_c1, duration, forwards)

        self.c2_rate = 0.0
        if self.end_c2:
            self.c2_rate = calc_c_rate(c2, end_c2, duration, forwards)


    def update(self, time):
        if not self.x2:
            self.x2 = self.length

        if self.last_update is None:
            self.last_update = time
            self.start_time = time
        else:
            t_delta = time - self.start_time
            self.last_update = time
            self.c1 = (self.start_c1 + t_delta * self.c1_rate) % 1.0
            self.c2 = (self.start_c2 + t_delta * self.c2_rate) % 1.0
        H = [0.0] * self.length
        c_rate = calc_c_rate(self.c1, self.c2, self.x2 - self.x1, self.forwards)
        for i in range(self.length):
            if i < self.x1:
                H[i] = self.c1
            elif i > self.x2:
                H[i] = self.c2
            else:
                H[i] = (self.c1 + c_rate * (i - self.x1)) % 1.0
        return zip(H, [self.sat] * self.length)

    def is_finished(self):
        return self.last_update - self.start_time > self.duration

if __name__ == '__main__':
    g = Gradient(c1 = .5,
                 c2 = 1.0,
                 end_c1 = 1.0,
                 end_c2 =.5,
                 forwards = False
                 )
    g.length = 20
    print g.update(0.0)
    print g.update(2.0)
    print g.update(4.0)
