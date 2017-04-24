import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')
sys.path.insert(0, myPath + '/../')
from console.lighting.gradient import Gradient
from track_info import TrackInfo
ID = '20UdW4qyeOmKa9YaOcv9WX'

ti = TrackInfo(ID)
high = False
kfs = []
for bt in ti.get_beats(0, 15.2):
    if high:
        kfs.append((bt, .65))
    else:
        kfs.append((bt, .4))
    high = not high
print kfs
main1 = []
