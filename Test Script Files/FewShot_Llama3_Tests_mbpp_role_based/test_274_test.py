import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 2)
        self.assertEqual(even_binomial_Coeff_Sum(4), 1)
        self.assertEqual(even_binomial_Coeff_Sum(5), 2)
        self.assertEqual(even_binomial_Coeff_Sum(6), 1)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(1.5)
