class SingleColor:

    def __init__(self, hue=1.0, saturation=1.0, nextc=[]):
        self.length = 64
        self.hue = hue
        self.saturation = saturation
        self.nextc = nextc

    def update(self, _):
        return zip([self.hue] * self.length, [self.saturation] * self.length)

    def is_finished(self):
        return False

class SingleIntensity:

    def __init__(self, i=1.0, nextc=[]):
        self.length = 64
        self.i = i
        self.nextc = nextc

    def update(self, _):
        return [self.i] * self.length

    def is_finished(self):
        return False
