import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 1)
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(5), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(100), 11)
        self.assertEqual(sum_div(1000), 12)

    def test_more_complex_cases(self):
        self.assertEqual(sum_div(10000), 11)
        self.assertEqual(sum_div(600851475143), 6857)
