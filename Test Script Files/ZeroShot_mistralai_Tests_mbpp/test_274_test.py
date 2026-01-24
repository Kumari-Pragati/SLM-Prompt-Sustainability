import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_even_binomial_Coeff_Sum_with_valid_input(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(3), 4)
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)
        self.assertEqual(even_binomial_Coeff_Sum(5), 16)
        self.assertEqual(even_binomial_Coeff_Sum(6), 32)
        self.assertEqual(even_binomial_Coeff_Sum(7), 64)
        self.assertEqual(even_binomial_Coeff_Sum(8), 128)
        self.assertEqual(even_binomial_Coeff_Sum(9), 256)
        self.assertEqual(even_binomial_Coeff_Sum(10), 512)

    def test_even_binomial_Coeff_Sum_with_negative_input(self):
        self.assertRaises(ValueError, even_binomial_Coeff_Sum, -1)

    def test_even_binomial_Coeff_Sum_with_non_integer_input(self):
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 2.5)
