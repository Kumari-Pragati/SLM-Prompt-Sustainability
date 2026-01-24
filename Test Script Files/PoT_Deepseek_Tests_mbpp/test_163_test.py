import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(5, 10), 125.0, places=1)

    def test_edge_case_with_zero_sides(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 10)

    def test_boundary_case_with_one_side(self):
        self.assertAlmostEqual(area_polygon(1, 10), 0.0, places=1)

    def test_corner_case_with_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-5, 10)

    def test_corner_case_with_negative_length(self):
        with self.assertRaises(ValueError):
            area_polygon(5, -10)

    def test_corner_case_with_zero_length(self):
        self.assertAlmostEqual(area_polygon(5, 0), 0.0, places=1)
