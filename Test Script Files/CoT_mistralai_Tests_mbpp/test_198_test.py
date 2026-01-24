import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.5980762113537759)
        self.assertAlmostEqual(largest_triangle(5, 12), 6.0)
        self.assertAlmostEqual(largest_triangle(10, 24), 19.617437908331684)

    def test_zero_and_non_positive_numbers(self):
        self.assertEqual(largest_triangle(0, 4), -1)
        self.assertEqual(largest_triangle(-3, 4), -1)
        self.assertEqual(largest_triangle(3, 0), -1)
        self.assertEqual(largest_triangle(0, 0), -1)

    def test_edge_cases(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 1.7320508075688772)
        self.assertAlmostEqual(largest_triangle(1, 2), 1.7320508075688772)
        self.assertAlmostEqual(largest_triangle(2, 1), 1.7320508075688772)
