import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(3, 5), 10.83, places=2)

    def test_edge_case_with_small_sides(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.5, places=2)

    def test_edge_case_with_large_sides(self):
        self.assertAlmostEqual(area_polygon(10, 100), 27777.78, places=2)

    def test_invalid_input_with_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-3, 5)

    def test_invalid_input_with_zero_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(0, 5)

    def test_invalid_input_with_negative_length(self):
        with self.assertRaises(ValueError):
            area_polygon(3, -5)

    def test_invalid_input_with_zero_length(self):
        with self.assertRaises(ValueError):
            area_polygon(3, 0)
