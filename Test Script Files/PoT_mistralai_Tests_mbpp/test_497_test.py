import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_cone(1, 2), math.pi * 5)

    def test_edge_case_zero_radius(self):
        self.assertEqual(surfacearea_cone(0, 1), math.pi)

    def test_edge_case_zero_height(self):
        self.assertEqual(surfacearea_cone(1, 0), math.pi * 2)

    def test_corner_case_negative_radius(self):
        self.assertEqual(surfacearea_cone(-1, 1), math.nan)

    def test_corner_case_negative_height(self):
        self.assertEqual(surfacearea_cone(1, -1), math.nan)
