import unittest
from mbpp_198_code import sqrt, pow

def largest_triangle(a, b):
    if a < 0 or b < 0:
        return -1
    area = (3 * sqrt(3) * pow(a, 2)) / (4 * b)
    return area

class TestLargestTriangle(unittest.TestCase):

    def test_negative_input(self):
        self.assertEqual(largest_triangle(-1, 1), -1)
        self.assertEqual(largest_triangle(1, -1), -1)

    def test_zero_input(self):
        self.assertEqual(largest_triangle(0, 1), 0)
        self.assertEqual(largest_triangle(1, 0), 0)

    def test_valid_input(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.5980762113537825)
        self.assertAlmostEqual(largest_triangle(4, 3), 2.5980762113537825)
        self.assertAlmostEqual(largest_triangle(5, 12), 6.0)
