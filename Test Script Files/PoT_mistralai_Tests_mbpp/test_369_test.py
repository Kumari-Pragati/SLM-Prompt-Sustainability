import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 18)

    def test_edge_case_zero(self):
        self.assertEqual(lateralsurface_cuboid(0, 2, 3), 0)

    def test_edge_case_negative(self):
        self.assertEqual(lateralsurface_cuboid(-1, 2, 3), 0)
        self.assertEqual(lateralsurface_cuboid(1, -2, 3), 0)
        self.assertEqual(lateralsurface_cuboid(1, 2, -3), 0)

    def test_boundary_case_one(self):
        self.assertEqual(lateralsurface_cuboid(1e-6, 2, 3), 18.000000000000002)

    def test_boundary_case_large(self):
        self.assertEqual(lateralsurface_cuboid(1e10, 2, 3), 600000000000018)
