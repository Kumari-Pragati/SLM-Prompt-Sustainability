import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 5), 84.7792838799752, places=5)

    def test_edge_case_zero_radius(self):
        self.assertEqual(surfacearea_cone(0, 5), 0)

    def test_boundary_case_zero_height(self):
        self.assertEqual(surfacearea_cone(3, 0), 0)

    def test_corner_case_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-3, 5)

    def test_corner_case_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(3, -5)

    def test_corner_case_large_numbers(self):
        self.assertAlmostEqual(surfacearea_cone(10000, 10000), 3141592653.589793, places=5)
