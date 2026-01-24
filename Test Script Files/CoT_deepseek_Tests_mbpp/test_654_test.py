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

    def test_negative_length_and_breadth(self):
        self.assertEqual(rectangle_perimeter(-5, -10), 0)

    def test_large_numbers(self):
        self.assertEqual(rectangle_perimeter(1000000, 2000000), 6000000)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", 10)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "10")
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", "10")
