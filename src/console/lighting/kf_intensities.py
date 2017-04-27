from math import cos, pi
class KFIntensities:

    def __init__(self, kfs, start_i=0.0):
        self.start_i = start_i
        self.kfs = kfs
        self.idx = 0
        self.last_update = None
        self.prevKF = (0.0, start_i)
        self.start_time = None
        self.nextKF = kfs[0]
        self.last_update = None
        self.type = 'intensity'

    def move_frames(self, currtime):
        t_delta = currtime - self.start_time
        for time, intensity in self.kfs[self.idx:]:
            if time <= t_delta and self.idx + 1 != len(self.kfs ):
                self.prevKF = (time, intensity)
                self.nextKF = self.kfs[self.idx+1]
                self.idx += 1


    def update(self, time):
        if self.start_time is None:
            self.start_time = time
        self.last_update = time
        self.move_frames(time)

        deltaT = self.nextKF[0] - self.prevKF[0]
        deltaI = self.nextKF[1] - self.prevKF[1]
        i0 = self.prevKF[1]
        if deltaI == 0:
            return [i0] * self.length
        t =  time - (self.prevKF[0] + self.start_time)

        i = .5*(1.0-cos(t*pi/deltaT))*deltaI + i0
        return [i] * self.length

    def is_finished(self):
        if self.last_update is None:
            return False
        return self.nextKF[0] <= self.last_update - self.start_time
