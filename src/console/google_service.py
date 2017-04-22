import requests
from light_engine import LightEngine
from models.module import LightModule
from models.strip import Strip
from lighting.wave import Wave
from lighting.basic import SingleColor, SingleIntensity
from lighting.color_transition import ColorTransition
from lighting.intensity_wave import IntensityWave
from lighting.home import (
    WARM_UP_COLOR,
    WARM_UP_I,
    OFF_I,
    ON_COLOR,
    ON_I
)
from config import Session
import time
URL = 'https://lights-164616.appspot.com/status'




session = Session()
modules = session.query(LightModule).all()
strips = session.query(Strip).all()
session.close()



time.sleep(2)
engine = LightEngine(modules, refresh_rate=30, debug=False)
r = requests.get(URL)
data = r.json()
print data
exit()
print "start color"
for strip in strips:
    strip.add_color_control(ON_COLOR)
    strip.add_intensity_control(ON_I)

time.sleep(5)
print "fade"
for strip in strips:
    strip.clear_add_color_control(WARM_UP_COLOR)
    strip.clear_add_intensity_control(WARM_UP_I)
time.sleep(8)

print 'off'
for strip in strips:
    strip.clear_add_intensity_control(OFF_I)
time.sleep(1)
exit()


while True:
    r = requests.get(URL)
    data = r.json()
    print data
    time.sleep(1)
    continue
    if not data['power']:
        for strip in Strips:
            strip.clear()
    else:
        if data['action'] == 'warmer':
            for strip in strips:
                warm_color = SingleColor(strip.length, hue=.04)
                c = ColorTransition(strip.length,
                                    start_color=.4,
                                    end_color=.04,
                                    nextc=[warm_color])
                strip.effects.append(c)
