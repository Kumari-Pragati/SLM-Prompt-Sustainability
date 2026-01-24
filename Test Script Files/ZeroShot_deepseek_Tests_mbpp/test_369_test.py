import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_lateralsurface_cuboid(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 22)
        self.assertEqual(lateralsurface_cuboid(5, 5, 5), 50)
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)
        self.assertEqual(lateralsurface_cuboid(10, 20, 30), 220)
        self.assertEqual(lateralsurface_cuboid(-1, -2, -3), -22)
