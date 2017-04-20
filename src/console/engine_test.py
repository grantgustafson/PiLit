from light_engine import LightEngine
from models.module import LightModule
from models.strip import Strip
from lighting.wave import Wave
from lighting.color_transition import ColorTransition
from lighting.intensity_wave import IntensityWave
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

    time.sleep(2)
    engine = LightEngine(modules)
    print 'beginning test'
    for strip in strips:
        strip.effects.append(ColorTransition(length=strip.length))
    time.sleep(6)
