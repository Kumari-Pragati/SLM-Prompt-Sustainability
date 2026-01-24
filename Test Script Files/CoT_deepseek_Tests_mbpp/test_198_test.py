import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(10, 2), 28.868747834589296)

    def test_negative_values(self):
        self.assertEqual(largest_triangle(-1, 2), -1)
        self.assertEqual(largest_triangle(1, -2), -1)
        self.assertEqual(largest_triangle(-1, -2), -1)

    def test_zero_values(self):
        self.assertEqual(largest_triangle(0, 2), 0)
        self.assertEqual(largest_triangle(1, 0), 0)
        self.assertEqual(largest_triangle(0, 0), 0)

    def test_large_values(self):
        self.assertAlmostEqual(largest_triangle(10000, 2), 7071067.707106771)
