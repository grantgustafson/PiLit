import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from models.light_modules import Modules
TEST_PATH = 'test_models.json'

class CreateModulesTestCase(unittest.TestCase):


    def test_create(self):
        modules = Modules(module_file_path=TEST_PATH)
        data = {'name': 'create test',
                'MAC' : 'mac',
                'numLEDs': 30,
                'location': 'kitchen'}
        module = modules.create(data)
        self.assertTrue(modules.get(name='create test') == module)
        self.assertTrue(modules.get(MAC='mac') == module)
    def tearDown(self):
        os.remove(TEST_PATH)

class RemoveModulesTestCase(unittest.TestCase):

    def test_remove(self):
        modules = Modules(module_file_path=TEST_PATH)
        data = {'name': 'remove test',
                'MAC' : 'mac',
                'numLEDs': 30,
                'location': 'kitchen'}
        module = modules.create(data)
        modules.delete(module)
        self.assertTrue(modules.get(name='remove test') == None)
        self.assertTrue(modules.get(MAC='mac') == None)

    def tearDown(self):
        os.remove(TEST_PATH)

class UpdateModulesTestCase(unittest.TestCase):

    def test_update(self):
        modules = Modules(module_file_path=TEST_PATH)
        data = {'name': 'name one',
                'MAC' : 'mac',
                'numLEDs': 30,
                'location': 'kitchen'}
        module = modules.create(data)
        self.assertTrue(modules.get(name='name one') == module)
        self.assertTrue(modules.get(MAC='mac') == module)
        module.name = 'name two'
        modules.update_modules()
        self.assertTrue(modules.get(name='name two') == module)
        self.assertTrue(modules.get(MAC='mac') == module)
        self.assertTrue(modules.get(name='name one') == None)

    def tearDown(self):
        os.remove(TEST_PATH)

if __name__ == '__main__':
    unittest.main()
