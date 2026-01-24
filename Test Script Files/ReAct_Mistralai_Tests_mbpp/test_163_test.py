import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_positive_sides_and_perimeter(self):
        self.assertAlmostEqual(area_polygon(3, 10), 75.0, delta=0.01)
        self.assertAlmostEqual(area_polygon(4, 20), 200.0, delta=0.01)

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(0, 10)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            area_polygon(-3, 10)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            area_polygon(3, 0)

    def test_small_sides(self):
        self.assertAlmostEqual(area_polygon(1, 2), 1.995, delta=0.01)

    def test_large_sides(self):
        self.assertAlmostEqual(area_polygon(1000, 2000), 1999999999.99, delta=1e9)

    def test_small_perimeter(self):
        self.assertAlmostEqual(area_polygon(3, 1), 3.005, delta=0.01)

    def test_large_perimeter(self):
        self.assertAlmostEqual(area_polygon(3, 1000000), 7499999999.99, delta=1e9)
