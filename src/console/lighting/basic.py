class Color:

    def __init__(self, hue=1.0, saturation=1.0):
        self.length = 64
        self.hue = hue
        self.saturation = saturation
        self.type = 'color'

    def update(self, _):
        return zip([self.hue] * self.length, [self.saturation] * self.length)

    def is_finished(self):
        return False

class Intensity:

    def __init__(self, i=1.0):
        self.length = 64
        self.i = i
        self.type = 'intensity'

    def update(self, _):
        return [self.i] * self.length

    def is_finished(self):
        return False
