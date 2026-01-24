import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_polygon(5, 10), 50)

    def test_zero_side_length(self):
        self.assertEqual(perimeter_polygon(0, 10), 0)

    def test_zero_number_of_sides(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_negative_side_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(-5, 10)

    def test_negative_number_of_sides(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(5, -10)
