import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_perimeter_polygon_typical(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_perimeter_polygon_zero_side(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_perimeter_polygon_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_perimeter_polygon_negative_side(self):
        self.assertEqual(perimeter_polygon(-5, 3), 15)

    def test_perimeter_polygon_negative_length(self):
        self.assertEqual(perimeter_polygon(5, -3), 15)

    def test_perimeter_polygon_zero_side_and_zero_length(self):
        self.assertEqual(perimeter_polygon(0, 0), 0)

    def test_perimeter_polygon_zero_side_and_negative_length(self):
        self.assertEqual(perimeter_polygon(0, -3), 0)

    def test_perimeter_polygon_negative_side_and_zero_length(self):
        self.assertEqual(perimeter_polygon(-5, 0), 0)

    def test_perimeter_polygon_negative_side_and_negative_length(self):
        self.assertEqual(perimeter_polygon(-5, -3), 15)
