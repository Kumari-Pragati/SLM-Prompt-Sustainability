import unittest
from mbpp_163_code import area_polygon
from math import tan, pi

class TestAreaPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(3, 5), 20.80083823052924, places=5)

    def test_edge_case_with_small_sides(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.5, places=5)

    def test_edge_case_with_large_sides(self):
        self.assertAlmostEqual(area_polygon(100, 100), 3141592.653589793, places=5)

    def test_error_case_with_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-3, 5)

    def test_error_case_with_zero_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(0, 5)

    def test_error_case_with_non_integer_sides(self):
        with self.assertRaises(TypeError):
            area_polygon(3.5, 5)

    def test_error_case_with_non_numeric_sides(self):
        with self.assertRaises(TypeError):
            area_polygon('3', 5)

    def test_error_case_with_non_numeric_length(self):
        with self.assertRaises(TypeError):
            area_polygon(3, '5')
