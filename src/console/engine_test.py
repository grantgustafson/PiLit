from light_engine import LightEngine
from models.module import LightModule
from models.strip import Strip
from lighting.wave import Wave, GradientWave, StandingWave
from lighting.color_transition import ColorTransition
from lighting.intensity_wave import IntensityWave
from lighting.gradient import Gradient
from lighting.basic import Intensity, Color
from lighting.strobe import Strobe, SmoothStrobe
from lighting.kf_intensities import KFIntensities
from lighting.ripple import Ripple
from config import Session
import time




if __name__ == '__main__':
    session = Session()

    modules = session.query(LightModule).all()
    strips = session.query(Strip).all()
    session.close()

    # time.sleep(2)
    # engine = LightEngine(modules)
    # print 'beginning test'
    # for i in range(5):
    #     for strip in strips:
    #         strip.effects.append(Wave(length=strip.length))
    #     time.sleep(3)

    time.sleep(1)
    engine = LightEngine(modules, refresh_rate=60)
    print 'beginning test'
    r = Ripple(speed=2)
    for strip in strips:
        strip.add_intensity_control(Ripple(speed=1, center = 60))
        strip.add_color_control(Color())
    time.sleep(14)
