import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cone(1, 2), math.pi * 3.0)
        self.assertEqual(lateralsurface_cone(2, 3), math.pi * 5.0)

    def test_edge_case_zero_height(self):
        self.assertEqual(lateralsurface_cone(1, 0), math.pi)

    def test_edge_case_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 1), 0)

    def test_corner_case_negative_radius(self):
        self.assertEqual(lateralsurface_cone(-1, 1), -math.pi)

    def test_corner_case_negative_height(self):
        self.assertEqual(lateralsurface_cone(1, -1), -math.pi)
