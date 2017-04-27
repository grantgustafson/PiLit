import unittest, os, sys, json
from copy import deepcopy
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')
sys.path.insert(0, myPath + '/../')
from track_info import TrackInfo
from config import (
    CHOREO_DATA_PATH
)
from show_data import KeyFrame, Control, Show
ID = '20UdW4qyeOmKa9YaOcv9WX'



ti = TrackInfo(ID)
high = False
kfs = []
show = Show()
show.main1 = []
show.main2 = []
for bt in ti.get_beats(0, 15.2):
    if high:
        kfs.append((bt, .65))
    else:
        kfs.append((bt, .4))
    high = not high
kfs.append((16.5, 0))
c1 = Control('KFIntensities', args=[kfs])
c2 = Control('Color', kwargs={'hue': .55})
kf = KeyFrame([c1, c2], time=0)
show.main2.append(kf)
show.main1.append(kf)

h_timing = [18.023 - 17.262, 20.103 - 19.323, 22.243 - 21.404, 24.423 - 23.605]
#print 'mean: ', (sum(h_timing) / len(h_timing))
beaton1s = ti.get_i_beat_in_bar(1, start_time=16.45, end_time=25)

sec_begin = 16.501
kfs = [(sec_begin, 0)]
interval = .4
color_kfs = []
colors = [1.0, .819, .902, 1.0]
for beat, color in zip(beaton1s, colors):
    kfs.append((beat - interval / 2, 0))
    color_kfs.append(KeyFrame([Control('Color', kwargs={'hue': color})], time=beat-.1, clear=True))
    for i in range(3):
        kfs.append((beat + interval * i, 1))
        kfs.append((beat + interval * i + interval / 2, 0))
beats = ti.get_beats(25.1, 34.51)
freq = 1.0 / (beats[1] - beats[0])
kfs.append((beats[0], .5))

kfs = map(lambda (x, y): (x-sec_begin, y), kfs)

c1 = Control('KFIntensities', args=[kfs])
kf = KeyFrame([c1], time=sec_begin, clear=True)
show.main2.append(kf)
show.main2 += color_kfs
show.main1.append(kf)
show.main1 += color_kfs

beats = ti.get_beats(25.1, 34.51)
freq = 1.0 / (beats[1] - beats[0])

start_time = 30
end_time = 48
c = Control('ColorTransition', kwargs={'h1': 0.0, 'h2': 0.5, 'duration': end_time - start_time})
kf = KeyFrame([c], time=start_time, clear=True)
show.main1.append(kf)
show.main2.append(kf)

c = Control('StandingWave', kwargs={'speed': freq, 'width': 128, 'min_i': .4, 'max_i': .8, 'duration': 20})
kf = KeyFrame([c], time=beats[0], clear=True)
show.main1.append(kf)
show.main2.append(kf)


curr_time = 34.5
end_time = 49.5
beats = ti.get_beats(curr_time, end_time)
beat_time = beats[1] - beats[0]

kfs = []
clear = True

while curr_time < end_time - .24:
    kfs.append(KeyFrame([Control('Wave', kwargs={'speed': 2.0, 'width': 30})], time=curr_time, clear=clear))
    curr_time += beat_time
    beat_time -= beat_time / 45
    clear = False

show.main1 += kfs
show.main2 += kfs
kf = KeyFrame([Control('Color', kwargs={'hue': .83})], time=end_time + .1, clear=True)
show.main1.append(kf)
show.main2.append(kf)

beat = ti.get_i_beat_in_bar(3, start_time=52, end_time=54)[0]
hit_time = .13

kfs = [(.01, 0), (beat - end_time - hit_time / 2, 0)]

hit4_pattern = []
for i in range(3):
    hit4_pattern.append((i * hit_time, 1.0))
    hit4_pattern.append((i * hit_time + hit_time / 2, .4))

kfs += map(lambda (t, i): (t + beat - end_time, i), hit4_pattern)

kfs1 = kfs
kfs2 = deepcopy(kfs)

next_hits2 = [54.665, 57.88, 62.16, 69.7, 71.84, 75.06, 79.345]
next_hits1 = [53.59, 56.81, 61.09, 63.23, 70.755, 73.98, 78.28, 80.44]
shift = .05

next_hits1 = map(lambda t: t - shift, next_hits1)
next_hits2 = map(lambda t: t - shift, next_hits2)

for nh in next_hits1:
    kfs1 += [(nh - end_time, .3)]
    kfs1 += map(lambda (t, i): (t + nh - end_time, i), hit4_pattern)

for nh in next_hits2:
    kfs2 += [(nh - end_time, .3)]
    kfs2 += map(lambda (t, i): (t + nh - end_time, i), hit4_pattern)

fade = [(85.6 - end_time, .7), (89.8 - end_time, .23)]
kfs1 += fade
kfs2 += fade

kf1 = KeyFrame([Control('KFIntensities', args=[kfs1])], time=end_time)
kf2 = KeyFrame([Control('KFIntensities', args=[kfs2])], time=end_time)

show.main1.append(kf1)
show.main2.append(kf2)

c = Control('ColorTransition', kwargs={'h1': 0.83, 'h2': 0.52, 'duration': 4, 'forwards': False})
kf = KeyFrame([c], time=82, clear=True)

show.main1.append(kf)
show.main2.append(kf)

c = Control('StandingWave', kwargs={'speed': .1, 'width': 64, 'min_i': .2, 'max_i': .55, 'duration': 13})
kf = KeyFrame([c], time=89, clear=True)
show.main1.append(kf)
show.main2.append(kf)

c1 = Control('ColorTransition', kwargs={'h1': 0.52, 'h2': 0.636, 'duration': 3, 'forwards': True})
c2 = Control('ColorTransition', kwargs={'h1': 0.52, 'h2': 0.9, 'duration': 3, 'forwards': True})
kf1 = KeyFrame([c1], time=99, clear=True)
kf2 = KeyFrame([c2], time=99, clear=True)




c = Control('Intensity', kwargs={'i': .45})
kf = KeyFrame([c], time = 102.6)
show.main1.append(kf)
show.main2.append(kf)




show.main1 = sorted(show.main1, key=lambda kf: kf.time)
show.main2 = sorted(show.main2, key=lambda kf: kf.time)
with open(os.path.join(CHOREO_DATA_PATH, ID), 'w') as f:
    json.dump(show.to_dict(), f, indent=4)
