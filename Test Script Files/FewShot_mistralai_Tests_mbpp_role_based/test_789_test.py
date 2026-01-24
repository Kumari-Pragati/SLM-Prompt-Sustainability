import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_positive_sides_and_lengths(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_zero_sides(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_negative_sides(self):
        self.assertRaises(ValueError, perimeter_polygon, -1, 3)

    def test_negative_length(self):
        self.assertRaises(ValueError, perimeter_polygon, 5, -3)
