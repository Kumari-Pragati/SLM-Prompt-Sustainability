import unittest
from mbpp_163_code import tan, pi
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_area_polygon_positive_values(self):
        self.assertAlmostEqual(area_polygon(3, 5), 20.80083823052924, places=5)
        self.assertAlmostEqual(area_polygon(4, 10), 225.0, places=5)
        self.assertAlmostEqual(area_polygon(5, 2), 5.89873847144314, places=5)

    def test_area_polygon_negative_values(self):
        self.assertRaises(ValueError, area_polygon, -3, 5)
        self.assertRaises(ValueError, area_polygon, 3, -5)
        self.assertRaises(ValueError, area_polygon, -3, -5)

    def test_area_polygon_zero_values(self):
        self.assertRaises(ValueError, area_polygon, 0, 5)
        self.assertRaises(ValueError, area_polygon, 3, 0)

    def test_area_polygon_non_integer_values(self):
        self.assertRaises(TypeError, area_polygon, 2.5, 5)
        self.assertRaises(TypeError, area_polygon, 3, 5.5)
