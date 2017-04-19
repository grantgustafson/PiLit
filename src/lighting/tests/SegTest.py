import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from strip import Strip
from module import Segment, Module

class EmptyModuleTest(unittest.TestCase):

    def test_empty_module(self):
        m = Module()
        self.assertTrue(m.render() == [])

    def test_empty_seg(self):
        num_pixels = 10
        s = Segment(10)
        for rgb in s.render():
            self.assertTrue(rgb == (0,0,0))

        m = Module()
        m.add_segment(s, 0)
        for rgb in s.render():
            self.assertTrue(rgb == (0,0,0))

        m = Module()
        m.add_segment(s, 10)
        pixels = m.render()
        self.assertTrue(len(pixels) == 20)
        for rgb in pixels:
            self.assertTrue(rgb == (0,0,0))

class BasicStripTest(unittest.TestCase):

    def test_single_seg(self):
        num_pixels = 10
        strip = Strip(num_pixels)
        s = Segment(num_pixels)
        s.add_strip(strip, 0, True)
        for rgb in s.render():
            self.assertTrue(rgb == (0,0,0))

    def test_two_seg(self):
        n1 = 10
        n2 = 5
        strip = Strip(n1 + n2)
        s1 = Segment(n1)
        s2 = Segment(n2)

        s1.add_strip(strip, 0, True)
        s2.add_strip(strip, n1 - 1, True)
        for rgb in s1.render():
            self.assertTrue(rgb == (0,0,0))
        for rgb in s2.render():
            self.assertTrue(rgb == (0,0,0))

class BasicMappingTest(unittest.TestCase):

    def test_map(self):
        n = 10
        strip = Strip(n * 2)
        s1 = Segment(n)
        s2 = Segment(n)
        s1.add_strip(strip, 0, True)
        s2.add_strip(strip, n, False)

        rgbs = [(i, 0, 0) for i in range(n*2)]
        strip.set_rgbs(rgbs)

        self.assertTrue(len(s1.render()) == n)
        for idx, rgb in enumerate(s1.render()):
            self.assertTrue(rgb == (idx, 0, 0))
        self.assertTrue(len(s2.render()) == n)
        for idx, rgb in enumerate(s2.render()):
            expected = n + (n - idx) - 1
            self.assertTrue(rgb == (expected, 0, 0))

    def test_seg_w_gap(self):
        n = 10
        strip = Strip(n * 3)
        s1 = Segment(n)
        s2 = Segment(n)
        s1.add_strip(strip, 0, True)
        s2.add_strip(strip, 2*n, False)

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)
        self.assertTrue(len(s1.render()) == n)
        for idx, rgb in enumerate(s1.render()):
            self.assertTrue(rgb == (idx, 0, 0))

        self.assertTrue(len(s2.render()) == n)
        for idx, rgb in enumerate(s2.render()):
            expected = 2*n + (n - idx) - 1
            self.assertTrue(rgb == (expected, 0, 0))

    def test_module_w_gap(self):
        n = 10
        strip = Strip(n * 3)
        s1 = Segment(n)
        s2 = Segment(n)
        s1.add_strip(strip, 0, True)
        s2.add_strip(strip, 2*n, False)

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)
        m = Module()
        m.add_segment(s1, 0)
        m.add_segment(s2, 2*n)
        for idx, rgb in enumerate(m.render()):
            if idx < 10:
                self.assertTrue(rgb == (idx, 0, 0))
            elif idx < 20:
                self.assertTrue(rgb == (0,0,0))
            else:
                self.assertTrue(rgb == ((5*n - idx - 1), 0, 0))

class ModuleStripTest(unittest.TestCase):

    def test_two_modules(self):
        n = 10
        strip = Strip(n * 2)
        s1 = Segment(n)
        s2 = Segment(n)
        s1.add_strip(strip, 0, True)
        s2.add_strip(strip, n, False)

        rgbs = [(i, 0, 0) for i in range(n*2)]
        strip.set_rgbs(rgbs)
        m1 = Module()
        m2 = Module()
        m1.add_segment(s1, 0)
        m2.add_segment(s2, 0)

        for idx, rgb in enumerate(m1.render()):
            self.assertTrue(rgb == (idx, 0, 0))

        for idx, rgb in enumerate(m2.render()):
            self.assertTrue(rgb == (2*n - idx - 1, 0, 0))
if __name__ == '__main__':
    unittest.main()
