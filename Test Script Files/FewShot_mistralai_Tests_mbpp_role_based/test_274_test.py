import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(4), 6)
        self.assertEqual(even_binomial_Coeff_Sum(10), 512)

    def test_zero(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)

    def test_negative_integer(self):
        self.assertRaises(ValueError, even_binomial_Coeff_Sum, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 3.14)
