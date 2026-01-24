import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_lateralsurface_cuboid(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(2, 3, 4), 24)
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 30)
        self.assertEqual(lateralsurface_cuboid(5, 6, 7), 84)
        self.assertEqual(lateralsurface_cuboid(10, 20, 30), 120)
        self.assertEqual(lateralsurface_cuboid(-1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(1, -2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(1, 2, -3), 12)
        self.assertEqual(lateralsurface_cuboid(1, 2, 0), 0)
        self.assertEqual(lateralsurface_cuboid(1, 2, 3.5), 14)
        self.assertEqual(lateralsurface_cuboid(1, 2, -3.5), 14)
