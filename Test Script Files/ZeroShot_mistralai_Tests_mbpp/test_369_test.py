import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):

    def test_lateral_surface_cuboid_positive(self):
        self.assertEqual(lateralsurface_cuboid(2, 3, 4), 32)
        self.assertEqual(lateralsurface_cuboid(4, 5, 6), 88)
        self.assertEqual(lateralsurface_cuboid(6, 7, 8), 144)

    def test_lateral_surface_cuboid_zero(self):
        self.assertEqual(lateralsurface_cuboid(0, 3, 4), 0)
        self.assertEqual(lateralsurface_cuboid(3, 0, 4), 0)
        self.assertEqual(lateralsurface_cuboid(3, 3, 0), 0)

    def test_lateral_surface_cuboid_negative(self):
        self.assertEqual(lateralsurface_cuboid(-2, 3, 4), 0)
        self.assertEqual(lateralsurface_cuboid(2, -3, 4), 0)
        self.assertEqual(lateralsurface_cuboid(2, 3, -4), 0)
