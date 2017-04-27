import sys, os, copy
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from console.lighting.gradient import Gradient
from console.lighting.basic import Color, Intensity
from console.lighting.color_transition import ColorTransition
from console.lighting.intensity_wave import IntensityWave
from console.lighting.kf_intensities import KFIntensities
from console.lighting.strobe import Strobe, SmoothStrobe
from console.lighting.wave import Wave, StandingWave, GradientWave
from console.lighting.ripple import Ripple
from console.lighting.multiplier import Multiplier
from console.lighting.pulsar import Pulsar


class Control(object):

    classes = {'Gradient': Gradient,
               'Color': Color,
               'Intensity': Intensity,
               'ColorTransition': ColorTransition,
               'IntensityWave': IntensityWave,
               'KFIntensities': KFIntensities,
               'Strobe': Strobe,
               'SmoothStrobe': SmoothStrobe,
               'Wave': Wave,
               'StandingWave': StandingWave,
               'GradientWave': GradientWave,
               'Ripple': Ripple,
               'Multiplier': Multiplier,
               'Pulsar': Pulsar}

    def __init__(self, name, args=[], kwargs={}):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def serialize_arg(self, arg):
        if type(arg) == Control:
            return arg.to_dict()
        else:
            return arg

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['args'] = [self.serialize_arg(arg) for arg in data['args']]
        data['kwargs'] = {k: self.serialize_arg(o) for (k,o) in data['kwargs'].items()}
        return data

    def create(self):
        C = self.classes[self.name]
        print self.kwargs
        return C(*self.args, **self.kwargs)

class KeyFrame:

    def __init__(self, controls, time, clear=False):
        self.controls = controls
        self.time = time
        self.clear = clear

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['controls'] = map(lambda c: c.to_dict(), data['controls'])
        return data

class Show:

    def to_dict(self):
        return {o: [t.to_dict() for t in getattr(self, o)] for o in self.__dict__}

    @staticmethod
    def parse_control(data):
        ctrl = Control.__new__(Control)
        data['args'] = [Show.parse_control(a) if type(a) is dict else a for a in data['args']]
        data['kwargs'] = {a : Show.parse_control(o) if type(a) is dict else o for (a, o) in data['kwargs'].items()}
        ctrl.__dict__ = data
        return ctrl

    def parse_kfs(self, kfs_data):
        kfs = []
        for kf in kfs_data:
            ctrls = map(Show.parse_control, kf['controls'])
            kfs.append(KeyFrame(ctrls, kf['time'], clear=kf['clear']))
        return kfs

    def load(self, data):
        for o in data:
            kfs = self.parse_kfs(data[o])
            setattr(self, o, kfs)



if __name__ == '__main__':
    kfs = [(0, .4), (1, .9)]
    c = Control('KFIntensities', args=[kfs])
    c2 = Control('Multiplier', args=[c])
    k = KeyFrame([c2], 0)
    show = Show()
    show.main1 = [k]
    data = show.to_dict()
    show = Show()
    show.load(data)
