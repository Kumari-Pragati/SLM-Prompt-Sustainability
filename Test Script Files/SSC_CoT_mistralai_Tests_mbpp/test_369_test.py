import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(5, 6, 7), 78)

    def test_edge_input(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)
        self.assertEqual(lateralsurface_cuboid(0, 0, 1), 2)
        self.assertEqual(lateralsurface_cuboid(1, 0, 0), 2)

    def test_negative_input(self):
        self.assertEqual(lateralsurface_cuboid(-1, 2, 3), -4)
        self.assertEqual(lateralsurface_cuboid(1, -2, 3), 0)
        self.assertEqual(lateralsurface_cuboid(1, 2, -3), 0)

    def test_float_input(self):
        self.assertAlmostEqual(lateralsurface_cuboid(1.5, 2.5, 3.5), 21.5)
