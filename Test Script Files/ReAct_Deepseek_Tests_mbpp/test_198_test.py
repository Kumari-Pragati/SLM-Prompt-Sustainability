import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(5, 10), 0.75 * math.sqrt(3) * 5**2 / 10)

    def test_zero_base(self):
        self.assertEqual(largest_triangle(0, 10), -1)

    def test_zero_height(self):
        self.assertEqual(largest_triangle(5, 0), -1)

    def test_negative_base(self):
        self.assertEqual(largest_triangle(-5, 10), -1)

    def test_negative_height(self):
        self.assertEqual(largest_triangle(5, -10), -1)

    def test_large_numbers(self):
        self.assertAlmostEqual(largest_triangle(1000, 2000), 0.75 * math.sqrt(3) * 1000**2 / 2000)

    def test_equality_with_math_formula(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 0.75 * math.sqrt(3) * 3**2 / 4)
