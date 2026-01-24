import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_perimeter_polygon_typical(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_perimeter_polygon_zero_side(self):
        with self.assertRaises(ZeroDivisionError):
            perimeter_polygon(0, 3)

    def test_perimeter_polygon_zero_length(self):
        with self.assertRaises(ZeroDivisionError):
            perimeter_polygon(5, 0)

    def test_perimeter_polygon_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(-5, 3)

    def test_perimeter_polygon_negative_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(5, -3)

    def test_perimeter_polygon_non_numeric_side(self):
        with self.assertRaises(TypeError):
            perimeter_polygon('five', 3)

    def test_perimeter_polygon_non_numeric_length(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(5, 'three')
