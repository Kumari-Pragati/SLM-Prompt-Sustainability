import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(3, 5), 20.800783046776805)

    def test_edge_case_with_small_polygon(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.5)

    def test_edge_case_with_large_polygon(self):
        self.assertAlmostEqual(area_polygon(1000, 1), 0.5)

    def test_edge_case_with_small_side_length(self):
        self.assertAlmostEqual(area_polygon(3, 0.001), 0.000012566370614359172)

    def test_edge_case_with_large_side_length(self):
        self.assertAlmostEqual(area_polygon(3, 1000000), 250000000000.0)

    def test_invalid_input_with_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-3, 5)

    def test_invalid_input_with_negative_side_length(self):
        with self.assertRaises(ValueError):
            area_polygon(3, -5)

    def test_invalid_input_with_zero_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(0, 5)
