import unittest, os, sys, json
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
kfs.append((25.1, .5))

kfs = map(lambda (x, y): (x-sec_begin, y), kfs)

c1 = Control('KFIntensities', args=[kfs])
c2 = Control('Color', kwargs={'hue': 1.0})
kf = KeyFrame([c1, c2], time=sec_begin, clear=True)
show.main1.append(kf)
show.main1 += color_kfs

with open(os.path.join(CHOREO_DATA_PATH, ID), 'w') as f:
    json.dump(show.to_dict(), f, indent=4)
