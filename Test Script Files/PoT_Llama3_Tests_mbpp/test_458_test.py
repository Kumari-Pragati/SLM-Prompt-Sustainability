import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_zero_length(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_zero_breadth(self):
        self.assertEqual(rectangle_area(4, 0), 0)

    def test_negative_length(self):
        self.assertEqual(rectangle_area(-4, 5), 20)

    def test_negative_breadth(self):
        self.assertEqual(rectangle_area(4, -5), 20)

    def test_zero_area(self):
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_non_integer_input(self):
        self.assertEqual(rectangle_area(4.5, 5.5), 22.5)
