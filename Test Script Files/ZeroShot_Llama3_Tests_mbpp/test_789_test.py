import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_perimeter_polygon_positive(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_perimeter_polygon_negative(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(-5, 3)

    def test_perimeter_polygon_zero(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(0, 3)

    def test_perimeter_polygon_non_numeric(self):
        with self.assertRaises(TypeError):
            perimeter_polygon('five', 3)

    def test_perimeter_polygon_non_numeric2(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(5, 'three')
