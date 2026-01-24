import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.5980762113537759)
        self.assertAlmostEqual(largest_triangle(6, 8), 5.196152422706632)

    def test_zero(self):
        self.assertAlmostEqual(largest_triangle(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(largest_triangle(-1, 1), -1)
        self.assertAlmostEqual(largest_triangle(1, -1), -1)
