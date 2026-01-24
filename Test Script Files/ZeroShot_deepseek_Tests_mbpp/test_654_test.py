import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(15, 20), 60)

    def test_negative_numbers(self):
        self.assertEqual(rectangle_perimeter(-5, -10), -30)
        self.assertEqual(rectangle_perimeter(-15, -20), -60)

    def test_zero(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(15, 0), 30)
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_decimal_numbers(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12)
        self.assertEqual(rectangle_perimeter(7.5, 10.5), 30)
