import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(4, 10), 2.5, places=2)

    def test_boundary_case_zero_N(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(0, 10)

    def test_boundary_case_zero_Sum(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 0), 0.0)

    def test_boundary_case_negative_N(self):
        with self.assertRaises(ValueError):
            Sum_of_Inverse_Divisors(-4, 10)

    def test_boundary_case_negative_Sum(self):
        with self.assertRaises(ValueError):
            Sum_of_Inverse_Divisors(4, -10)

    def test_edge_case_large_numbers(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(10**6, 10**6), 1.0, places=2)
