import sys, os, time, json
from light_engine import LightEngine
from models.module import LightModule
from models.strip import Strip
from os.path import join
from config import Session
from opc import Client
import threading
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../choreographer')
from show_data import Show, KeyFrame, Control
from spotify import Spotify

CDP = '../choreographer/choreos/data'
TID = '20UdW4qyeOmKa9YaOcv9WX'
REFRESH_RATE = 50
SIM = True

class Driver:

    def __init__(self):
        print 'Initializing Driver'
        session = Session()
        self.modules = session.query(LightModule).all()
        self.strips = {s.name: s for s in session.query(Strip).all()}
        session.close()
        print 'starting engine'

        self.engine = LightEngine(self.modules)
        print 'engine running'
        self.sp = Spotify()
        print 'spotify loaded'
        if SIM:
            self.sim = Client('127.0.0.1:7890')

    def act_on_kf(self, kf, strip):
        for ctrl in kf.controls:
            ctrl = ctrl.create()
            if ctrl.type == 'intensity':
                strip.add_intensity_control(ctrl, clear=kf.clear)
            if ctrl.type == 'color':
                strip.add_color_control(ctrl, clear=kf.clear)
                print strip.color_controls
            if ctrl.type == 'combo':
                strip.add_combo_control(ctrl, clear=kf.clear)

    def run(self, track_id):
        with open(join(CDP, track_id)) as f:
            data = json.load(f)
            print data
        show = Show()
        show.load(data)
        self.show = show
        #self.visited_kfs = set()
        self.idxs = {str(o) : 0 for o in show.__dict__}
        self.start_pos = self.sp.get_player_pos()
        self.start_time = time.time() - self.start_pos
        self.update()

    def update_strip(self, strip, time):
        curr_idx = self.idxs[strip.name]
        kfs = getattr(self.show, strip.name)
        if len(kfs) == 0:
            return
        for kf in kfs[curr_idx:]:
            if kf.time <= time:
                self.act_on_kf(kf, strip)
                #self.visited_kfs.add(kf)
                curr_idx += 1
        self.idxs[strip.name] = curr_idx

    def update(self):
        curr_time = time.time() - self.start_time
        if SIM:
            pixels = []
        for o in self.show.__dict__:
            strip = self.strips[o]
            self.update_strip(strip, curr_time)
            if SIM:
                strip.compile(curr_time)
                pixels += strip.compiled_rgb
        if SIM:
            self.sim.put_pixels(pixels)
        t = threading.Timer(1.0/REFRESH_RATE, self.update)
        t.setDaemon(True)
        t.start()



if __name__ == '__main__':
    driver = Driver()
    print 'running: {}'.format(TID)
    driver.run(TID)
    while True:
        pass
    # engine = LightEngine(modules, refresh_rate=60)
