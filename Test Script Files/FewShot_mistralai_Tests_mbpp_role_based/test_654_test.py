import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):
    def test_positive_length_and_width(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)

    def test_zero_length_and_width(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_negative_length_and_positive_width(self):
        self.assertEqual(rectangle_perimeter(-2, 3), 10)

    def test_positive_length_and_negative_width(self):
        self.assertEqual(rectangle_perimeter(2, -3), 10)

    def test_negative_length_and_negative_width(self):
        self.assertEqual(rectangle_perimeter(-2, -3), 10)
