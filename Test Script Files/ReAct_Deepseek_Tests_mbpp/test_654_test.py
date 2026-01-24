import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_zero_length_or_breadth(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(5, 0), 10)

    def test_negative_length_or_breadth(self):
        self.assertEqual(rectangle_perimeter(-5, 10), 20)
        self.assertEqual(rectangle_perimeter(5, -10), 10)
        self.assertEqual(rectangle_perimeter(-5, -10), 0)

    def test_large_numbers(self):
        self.assertEqual(rectangle_perimeter(10000, 20000), 60000)
