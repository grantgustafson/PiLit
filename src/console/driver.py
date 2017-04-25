import sys, os, time, json
from light_engine import LightEngine
from models.module import LightModule
from models.strip import Strip
from os.path import join
from config import Session
import threading
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../choreographer')
from show_data import Show, KeyFrame, Control

CDP = '../choreographer/choreos/data'
TID = '20UdW4qyeOmKa9YaOcv9WX'
REFRESH_RATE = 30

class Driver:

    def __init__(self):
        session = Session()
        self.modules = session.query(LightModule).all()
        self.strips = {s.name: s for s in session.query(Strip).all()}
        session.close()
        self.engine = LightEngine(self.modules)

    def act_on_kf(self, kf, strip):
        for ctrl in kf.controls:
            ctrl = ctrl.create()
            if ctrl.type == 'intensity':
                strip.add_intensity_control(ctrl, kf.clear)
            if ctrl.type == 'color':
                strip.add_color_control(ctrl, kf.clear)
            if ctrl.type == 'combo':
                strip.add_combo_control(ctrl, kf.clear)

    def run(self, track_id):
        with open(join(CDP, track_id)) as f:
            data = json.load(f)
        show = Show()
        show.load(data)
        self.show = show
        #self.visited_kfs = set()
        self.idxs = {str(o) : 0 for o in show.__dict__}
        self.start_time = time.time()
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
        for o in self.show.__dict__:
            strip = self.strips[o]
            self.update_strip(strip, curr_time)
        t = threading.Timer(1.0/REFRESH_RATE, self.update)
        t.setDaemon(True)
        t.start()



if __name__ == '__main__':
    driver = Driver()
    driver.run(TID)
    time.sleep(25)
    # engine = LightEngine(modules, refresh_rate=60)
