import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_binomial_Coeff_Sum(5), 16)

    def test_boundary_conditions(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 4)

    def test_large_numbers(self):
        self.assertEqual(even_binomial_Coeff_Sum(10), 1024)

    def test_zero_input(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            even_binomial_Coeff_Sum(-5)
