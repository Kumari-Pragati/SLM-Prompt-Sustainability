import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSum_of_Inverse_Divisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100), 10.0)

    def test_edge_case_N_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(0, 100)

    def test_edge_case_Sum_zero(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 0), 0.0)

    def test_edge_case_N_and_Sum_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(0, 0)

    def test_edge_case_N_negative(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(-10, 100)

    def test_edge_case_Sum_negative(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(10, -100)

    def test_edge_case_N_and_Sum_negative(self):
        with self.assertRaises(ZeroDivisionError):
            Sum_of_Inverse_Divisors(-10, -100)
