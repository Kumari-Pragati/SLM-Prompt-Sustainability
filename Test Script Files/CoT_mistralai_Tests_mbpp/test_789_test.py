import unittest
from mbpp_789_code import tan, pi
from789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_perimeter_of_square(self):
        self.assertEqual(perimeter_polygon(4, 5), 20)

    def test_perimeter_of_regular_pentagon(self):
        self.assertEqual(perimeter_polygon(5, 2*pi/5), 10)

    def test_perimeter_of_regular_hexagon(self):
        self.assertEqual(perimeter_polygon(6, 2*pi/6), 12)

    def test_perimeter_of_irregular_polygon(self):
        self.assertEqual(perimeter_polygon(7, 7), 49)

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(0, 1)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(1, 0)
