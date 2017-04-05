import os
from config import (
    LOGGER,
)
MODULE_FILE_PATH = 'modules.json'


def create_module_file():
    open(MODULE_FILE_PATH, 'x').write('[]').close()

def parse_modules(data):
    for module_json in data:
        if 'MAC' not in module_json:
            LOGGER.error('')

def init():
    LOGGER.info('initializing light modules')
    global modules
    modules = []

    if not os.path.isfile(MODULE_FILE_PATH):
        LOGGER.info('module file does not exist, creating it')
        create_module_file()

    with open(MODULE_FILE_PATH, 'r') as f:
        raw_json = f.read()

    try:
        module_json = json.loads(raw_json)
    except ValueError, e:
        # empty or erroneous module file
        LOGGER.warning('module file not valid JSON')

init()

class Light_Module:

    def __init__(self, MAC)
        self._MAC = MAC
