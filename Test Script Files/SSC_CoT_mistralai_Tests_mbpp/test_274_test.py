import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)
        self.assertEqual(even_binomial_Coeff_Sum(6), 32)

    def test_edge_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 3)
        self.assertEqual(even_binomial_Coeff_Sum(5), 16)

    def test_negative_input(self):
        self.assertRaises(ValueError, even_binomial_Coeff_Sum, -1)
        self.assertRaises(ValueError, even_binomial_Coeff_Sum, -2)

    def test_float_input(self):
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 2.5)
