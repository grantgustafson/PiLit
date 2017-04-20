import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from models.strip import Strip
from models.module import LightModule
from models.segment import Segment

class EmptyModuleTest(unittest.TestCase):

    def test_empty_module(self):
        m = LightModule()
        time = 0
        self.assertTrue(m.render(time) == [])

    def test_empty_seg(self):
        num_pixels = 10
        time = 0
        s = Segment(num_pixels=10)
        for rgb in s.render(time):
            self.assertTrue(rgb == (0,0,0))

        m = LightModule(hostname='h', location='l')
        m.segments = [s]
        for rgb in s.render(time):
            self.assertTrue(rgb == (0,0,0))

        s.module_startpixel = 10
        pixels = m.render(time)
        self.assertTrue(len(pixels) == 20)
        for rgb in pixels:
            self.assertTrue(rgb == (0,0,0))

class BasicStripTest(unittest.TestCase):

    def test_single_seg(self):
        num_pixels = 10
        time = 0
        strip = Strip(length=num_pixels)
        s = Segment(num_pixels=num_pixels,
                    module_startpixel=0,
                    strip_startpixel=0,
                    forwards=True)
        strip.segments = [s]
        for rgb in s.render(time):
            self.assertTrue(rgb == (0,0,0))

    def test_two_seg(self):
        n1 = 10
        n2 = 5
        time = 0
        strip = Strip(n1 + n2)
        s1 = Segment(n1, strip_startpixel=0)
        s2 = Segment(n2, strip_startpixel=n1)

        strip.segments = [s1, s2]

        self.assertTrue(len(s1.render(time)) == n1)
        for rgb in s1.render(time):
            self.assertTrue(rgb == (0,0,0))
        self.assertTrue(len(s2.render(time)) == n2)
        for rgb in s2.render(time):
            self.assertTrue(rgb == (0,0,0))

class BasicMappingTest(unittest.TestCase):

    def test_seg_map(self):
        n = 10
        time = 0
        strip = Strip(n * 2)
        s1 = Segment(n, strip_startpixel=0)
        s2 = Segment(n, strip_startpixel=n, forwards=False)

        rgbs = [(i, 0, 0) for i in range(n*2)]
        strip.set_rgbs(rgbs)
        strip.segments = [s1, s2]

        self.assertTrue(len(s1.render(time)) == n)
        for idx, rgb in enumerate(s1.render(time)):
            self.assertTrue(rgb == (idx, 0, 0))
        self.assertTrue(len(s2.render(time)) == n)
        for idx, rgb in enumerate(s2.render(time)):
            expected = n + (n - idx) - 1
            self.assertTrue(rgb == (expected, 0, 0))

    def test_seg_w_gap(self):
        n = 10
        time = 0
        strip = Strip(n * 3)
        s1 = Segment(n, strip_startpixel=0)
        s2 = Segment(n, strip_startpixel=2*n, forwards=False)
        strip.segments = [s1, s2]

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)
        self.assertTrue(len(s1.render(time)) == n)
        for idx, rgb in enumerate(s1.render(time)):
            self.assertTrue(rgb == (idx, 0, 0))

        self.assertTrue(len(s2.render(time)) == n)
        for idx, rgb in enumerate(s2.render(time)):
            expected = 2*n + (n - idx) - 1
            self.assertTrue(rgb == (expected, 0, 0))

    def test_module_w_gap(self):
        n = 10
        time = 0
        strip = Strip(n * 3)
        s1 = Segment(n, strip_startpixel=0)
        s2 = Segment(n, strip_startpixel=2*n, module_startpixel=2*n, forwards=False)
        strip.segments = [s1, s2]

        m = LightModule(hostname='test', location='l')
        m.segments = [s1, s2]

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)
        self.assertTrue(len(m.render(time)) == 3*n)
        for idx, rgb in enumerate(m.render(time)):
            if idx < 10:
                self.assertTrue(rgb == (idx, 0, 0))
            elif idx < 20:
                self.assertTrue(rgb == (0,0,0))
            else:
                self.assertTrue(rgb == ((5*n - idx - 1), 0, 0))

class ModuleStripTest(unittest.TestCase):

    def test_two_modules(self):
        n = 10
        time = 0
        strip = Strip(n * 3)
        s1 = Segment(n, strip_startpixel=0)
        s2 = Segment(n, strip_startpixel=2*n, forwards=False)
        strip.segments = [s1, s2]

        m1 = LightModule(hostname='test1', location='l')
        m1.segments = [s1]

        m2 = LightModule(hostname='test2', location='l')
        m2.segments = [s2]

        rgbs = [(i, 0, 0) for i in range(n*3)]
        strip.set_rgbs(rgbs)
        for idx, rgb in enumerate(m1.render(time)):
            self.assertTrue(rgb == (idx, 0, 0))

        for idx, rgb in enumerate(m2.render(time)):
            self.assertTrue(rgb == (3*n - idx - 1, 0, 0))
if __name__ == '__main__':
    unittest.main()
