import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter_polygon(5, 3), 30)

    def test_perimeter_negative_sides(self):
        self.assertEqual(perimeter_polygon(-5, 3), 30)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_perimeter_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_perimeter_non_numeric_sides(self):
        with self.assertRaises(TypeError):
            perimeter_polygon('five', 3)

    def test_perimeter_non_numeric_length(self):
        with self.assertRaises(TypeError):
            perimeter_polygon(5, 'three')
