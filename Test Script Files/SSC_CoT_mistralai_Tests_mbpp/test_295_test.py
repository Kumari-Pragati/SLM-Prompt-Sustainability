import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(24), 8)
        self.assertEqual(sum_div(10), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 2)
        self.assertEqual(sum_div(4), 2)
        self.assertEqual(sum_div(5), 1)
        self.assertEqual(sum_div(15), 4)
        self.assertEqual(sum_div(20), 4)
        self.assertEqual(sum_div(21), 1)

    def test_special_cases(self):
        self.assertEqual(sum_div(12), 6)  # perfect squares
        self.assertEqual(sum_div(20), 4)  # perfect squares
        self.assertEqual(sum_div(28), 14)  # composite number with two distinct prime factors
