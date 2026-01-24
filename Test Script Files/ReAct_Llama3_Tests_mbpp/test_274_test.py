import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 0)

    def test_positive(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 6)
        self.assertEqual(even_binomial_Coeff_Sum(5), 10)

    def test_negative(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(3.5)
