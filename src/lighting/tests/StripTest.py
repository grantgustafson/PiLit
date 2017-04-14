import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from light_strip import Strip

class StripMappingTest(unittest.TestCase):

    def test_basic_map(self):
        mapping = [{'startpixel':0, 'numpixels': 10, 'forwards': True}]
        s = Strip(mapping)
        for i in range(10):
            self.assertTrue(s.mapping[i] == i)

    def test_moderate_map(self):
        mapping = [{'startpixel':9, 'numpixels': 10, 'forwards': False},
                   {'startpixel':10, 'numpixels': 10, 'forwards': True}]
        s = Strip(mapping)
        print s.mapping
        for i in range(10):
            self.assertTrue(s.mapping[i] == (9 - i))
        for i in range(10, 10):
            self.assertTrue(s.mapping[i] == i)

    def test_gap_map(self):
        mapping = [{'startpixel':9, 'numpixels': 10, 'forwards': False},
                   {'startpixel':20, 'numpixels': 10, 'forwards': True}]
        s = Strip(mapping)
        print s.mapping
        for i in range(10):
            self.assertTrue(s.mapping[i] == (9 - i))
        for i in range(20, 10):
            self.assertTrue(s.mapping[i] == i)
            
if __name__ == '__main__':
    unittest.main()
