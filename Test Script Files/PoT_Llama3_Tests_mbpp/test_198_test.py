import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(5, 10), 2.5)

    def test_edge_case_a_zero(self):
        self.assertEqual(largest_triangle(0, 10), -1)

    def test_edge_case_b_zero(self):
        self.assertEqual(largest_triangle(5, 0), -1)

    def test_edge_case_a_negative(self):
        self.assertEqual(largest_triangle(-5, 10), -1)

    def test_edge_case_b_negative(self):
        self.assertEqual(largest_triangle(5, -10), -1)

    def test_edge_case_a_and_b_zero(self):
        self.assertEqual(largest_triangle(0, 0), -1)

    def test_edge_case_a_and_b_negative(self):
        self.assertEqual(largest_triangle(-5, -10), -1)
