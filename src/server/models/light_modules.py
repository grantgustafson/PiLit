import os, json
from light_module import Light_Module
from hosts import Hosts
from jsonschema import validate
import jsonschema
from config import (
    LOGGER,
    MODULE_FILE_PATH,
    MODULE_SCHEMA_PATH,
)

class Modules:
    _shared_state = {}
    _instantiated = False
    def __init__(self, module_file_path=MODULE_FILE_PATH):
        self.__dict__ = self._shared_state
        if not self._instantiated:
            LOGGER.info('initializing light modules')
            self._module_file_path = module_file_path
            self._check_environ()
            self._load_schema()
            self._MAC_map = {}
            self._name_map = {}
            self._load_modules()
            self._hosts = Hosts(self)
            self._unconfigured_hosts = {}
            self._hosts.start_detection()
            self._instantiated = True

    def update_modules(self):
        self._name_map = {}
        for module in self.modules:
            self._name_map[module.name] = module
        self._write_modules()

    def add_unconfigured_host(self, name, mac, ip):
        self._unconfigured_hosts[mac] = (name, ip)

    def _unconfigured_to_json(self, mac):
        return {'MAC': mac,
                'ip' : self._unconfigured_hosts[mac][1],
                'name' : self._unconfigured_hosts[mac][0]}

    def get_unconfigured_json(self):
        return [self._unconfigured_to_json(k) for k in self._unconfigured_hosts]

    def get_host(self, name):
        for k in self._unconfigured_hosts:
            if self._unconfigured_hosts[k][0] == name:
                return self._unconfigured_to_json(k)
        return None

    def create(self, data):
        if self.validate_module(data):
            module = Light_Module(data, self.schema)
            self.modules.append(module)
            self._write_modules()
            self._MAC_map[module.MAC] = module
            self._name_map[module.name] = module
            return module
        return None

    def delete(self, module):
        self.modules.remove(module)
        del self._MAC_map[module.MAC]
        del self._name_map[module.name]
        self._write_modules()

    def get(self, MAC=None, name=None):
        if MAC and MAC in self._MAC_map:
            return self._MAC_map[MAC]
        if name and name in self._name_map:
            return self._name_map[name]
        return None

    def _load_modules(self):
        with open(self._module_file_path, 'r') as f:
            raw_json = f.read()

        try:
            module_json = json.loads(raw_json)
            self.validate_modules(module_json)
            self.modules = []
            for data in module_json:
                module = Light_Module(data, self.schema)
                self._MAC_map[module.MAC] = module
                self._name_map[module.name] = module
                self.modules.append(module)
        except ValueError, e:
            # empty or erroneous module file
            LOGGER.warning('Module file {} not valid JSON'.format(self._module_file_path))

    def _load_schema(self):
        with open(MODULE_SCHEMA_PATH) as f:
            self.schema = json.load(f)

    def _create_module_file(self):
        with open(self._module_file_path, 'w') as f:
            f.write('[]')

    def _write_modules(self):
        module_json = json.dumps(self.modules, default=lambda o: o.to_dict(),
                                    sort_keys=True, indent=4)
        with open(self._module_file_path, 'w') as f:
            f.write(module_json)

    def get_model_json(self):
        return [o.to_web_dict() for o in self.modules]

    def validate_modules(self, modules):
        for module in modules:
            if not self.validate_module(module):
                return False
        return True

    def validate_module(self, module):
        try:
            validate(module, self.schema)
            return True
        except jsonschema.exceptions.ValidationError as ve:
            LOGGER.error('Module data error: {}').format(ve)
            return False

    def _check_environ(self):
        if not os.path.isfile(self._module_file_path):
            LOGGER.info('module file does not exist, creating it')
            self._create_module_file()
