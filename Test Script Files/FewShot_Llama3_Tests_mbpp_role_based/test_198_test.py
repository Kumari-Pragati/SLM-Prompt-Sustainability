import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(largest_triangle(5, 10), 12.5)

    def test_zero(self):
        self.assertEqual(largest_triangle(0, 10), -1)

    def test_negative_numbers(self):
        self.assertEqual(largest_triangle(-5, 10), -1)

    def test_zero_area(self):
        self.assertEqual(largest_triangle(5, 0), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_triangle("a", 10)
