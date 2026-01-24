import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCones(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(5, 10), 3.141592653589793*5*15)

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 10), 0)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(5, 0), 0)

    def test_edge_case_zero_radius_and_height(self):
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-5, 10)

    def test_edge_case_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(5, -10)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_cone('five', 10)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cone(5, 'ten')
