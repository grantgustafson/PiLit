from math import ceil, sin, cos, pi, floor
class Pulsar:

    def __init__(self, kfs, center, smoothness=4, i=1.0, ):
        self.kfs = kfs
        self.center = center
        self.i = i
        self.idx = 0
        self.prevKF = (0.0, 0.0)
        self.nextKF = kfs[0]
        self.smoothness = smoothness
        self.last_update = None
        self.start_time = None
        self.type = 'intensity'

    def move_frames(self, currtime):
        t_delta = currtime - self.start_time
        for time, d in self.kfs[self.idx:]:
            if time <= t_delta and self.idx + 1 != len(self.kfs ):
                self.prevKF = (time, d)
                self.nextKF = self.kfs[self.idx+1]
                self.idx += 1

    def create_I(self, d):
        I = [0.0] * self.length
        num_pixels = int(floor(2*d))
        x0 = int(ceil(self.center - d))
        if d < self.smoothness:
            for i in range(num_pixels):
                x = x0 + i
                if x >= 0 and x < self.length:
                    I[x] = .5*(1.0 + cos((i/2*d - 1.0)*pi)) * self.i
        else:
            smooth_pixels = int(floor(self.smoothness))
            for i in range(smooth_pixels):
                x = x0 + i
                v = x - self.center + (d - self.smoothness)
                if x >= 0 and x < self.length:
                    I[x] = .5*(1.0 + cos(v/self.smoothness*pi)) * self.i
            x1 = int(floor(self.center + d))
            for i in range(x0 + smooth_pixels, x1 - smooth_pixels + 1):
                if i >= 0 and i < self.length:
                    I[i] = self.i
            for i in range(smooth_pixels):
                x = x1 - i
                v = x - self.center - d + self.smoothness
                if x >= 0 and x < self.length:
                    I[x] = .5*(1.0 + cos(v/self.smoothness*pi)) * self.i
        return I

    def update(self, time):
        if self.start_time is None:
            self.start_time = time
        self.last_update = time
        self.move_frames(time)

        deltaT = self.nextKF[0] - self.prevKF[0]
        deltaD = self.nextKF[1] - self.prevKF[1]
        d0 = self.prevKF[1]

        I = [0.0] * self.length
        if deltaD == 0:
            return self.create_I(d0)

        t =  time - (self.prevKF[0] + self.start_time)

        d = .5*(1.0-cos(t*pi/deltaT))*deltaD + d0

        return self.create_I(d)

        def is_finished(self):
            if self.last_update is None:
                return False
            return self.nextKF[0] <= self.last_update - self.start_time

if __name__ == "__main__":
    import time

    kfs = [(0, 0), (1, 10), (2, 6), (4, 20)]
    p = Pulsar(kfs, 20)
    p.length = 40

    print p.update(0)
    print p.update(1)
    print p.update(1.5)
    print p.update(2)
    print p.update(3)
    print p.update(4)
