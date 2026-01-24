import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_area_polygon_positive_s(self):
        self.assertAlmostEqual(area_polygon(3, 1), 3.0, places=5)

    def test_area_polygon_negative_s(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(-3, 1)

    def test_area_polygon_zero_s(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 1)

    def test_area_polygon_zero_l(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(3, 0)

    def test_area_polygon_zero_s_and_l(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 0)

    def test_area_polygon_non_numeric_s(self):
        with self.assertRaises(TypeError):
            area_polygon('a', 1)

    def test_area_polygon_non_numeric_l(self):
        with self.assertRaises(TypeError):
            area_polygon(3, 'b')

    def test_area_polygon_non_numeric_s_and_l(self):
        with self.assertRaises(TypeError):
            area_polygon('a', 'b')
