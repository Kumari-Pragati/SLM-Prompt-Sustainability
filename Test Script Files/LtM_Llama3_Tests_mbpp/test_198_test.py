import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(largest_triangle(1, 1), 1.0)
        self.assertEqual(largest_triangle(2, 2), 2.0)
        self.assertEqual(largest_triangle(3, 3), 3.0)

    def test_negative_inputs(self):
        self.assertEqual(largest_triangle(-1, 1), -1)
        self.assertEqual(largest_triangle(1, -1), -1)
        self.assertEqual(largest_triangle(-1, -1), -1)

    def test_zero_inputs(self):
        self.assertEqual(largest_triangle(0, 1), -1)
        self.assertEqual(largest_triangle(1, 0), -1)
        self.assertEqual(largest_triangle(0, 0), -1)

    def test_edge_cases(self):
        self.assertEqual(largest_triangle(10, 10), 10.0)
        self.assertEqual(largest_triangle(100, 100), 100.0)
