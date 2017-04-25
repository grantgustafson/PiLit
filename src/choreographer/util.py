import imp, inspect, sys, os
from os.path import join
from os import listdir
MOD_PATH = './../console/lighting'
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + MOD_PATH)

path = join(myPath, MOD_PATH, 'control.py')
BASE = getattr(imp.load_source('control', path), 'Control')
from util import calc_c_rate
def load_module_controls(name):
    mod = imp.load_source(name, join(MOD_PATH, name))
    return inspect.getmembers(mod, _is_ctrl_class())

def get_mod_names():
    return filter(lambda n: not n.startswith('.') \
                    and n.endswith('.py') \
                    and n != 'util.py',
                 listdir(MOD_PATH))

def _is_ctrl_class():
    def fn(c):
        return inspect.isclass(c) and issubclass(c, BASE) and c != base_action

    return fn

if __name__ == '__main__':
    for name in get_mod_names():
        print load_module_controls(name)
