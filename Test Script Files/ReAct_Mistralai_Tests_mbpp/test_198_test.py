import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.5980762113537759)
        self.assertAlmostEqual(largest_triangle(5, 12), 6.0)
        self.assertAlmostEqual(largest_triangle(10, 24), 19.617437908331673)

    def test_zero_and_non_positive_numbers(self):
        self.assertEqual(largest_triangle(0, 4), -1)
        self.assertEqual(largest_triangle(-3, 4), -1)
        self.assertEqual(largest_triangle(3, 0), -1)

    def test_small_base(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 1.7320508075688772)
        self.assertAlmostEqual(largest_triangle(2, 2), 2.414213562373095)

    def test_large_base(self):
        self.assertAlmostEqual(largest_triangle(1000, 1000), 999999.9999999999)
