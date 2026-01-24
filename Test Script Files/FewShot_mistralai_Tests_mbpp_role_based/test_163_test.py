import unittest
from mbpp_163_code import tan, pi
from 163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_positive_sides_and_lengths(self):
        self.assertAlmostEqual(area_polygon(3, 4), 3 * (4 ** 2) / (4 * tan(pi / 3)))

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(0, 1)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-1, 2)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            area_polygon(2, 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            area_polygon(3, -1)
