
class Strip:

    def __init__(self, length):
        self._length = length
        self._hsv = []
        self._compiled_rgb = [(0,0,0)]*length

    def compile(self):
        pass

    def set_rgbs(self, rgbs):
        if not len(rgbs) == self._length:
            #TODO throw error
            return
        self._compiled_rgb = rgbs

    def get_rgb(self):
        return self._compiled_rgb

    def __getitem__(self, key):
        return self._compiled_rgb[key]
