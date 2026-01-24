import unittest
from mbpp_789_code import tan, pi
from 789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_perimeter_polygon_with_positive_values(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)
        self.assertEqual(perimeter_polygon(10, 4), 40)
        self.assertEqual(perimeter_polygon(2 * pi, 1), 2 * pi)

    def test_perimeter_polygon_with_zero_side_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(5, 0)

    def test_perimeter_polygon_with_negative_side_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(5, -3)
