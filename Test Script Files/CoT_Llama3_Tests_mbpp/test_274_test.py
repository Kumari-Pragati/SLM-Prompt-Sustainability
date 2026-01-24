import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_even_binomial_Coeff_Sum_positive(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 3)
        self.assertEqual(even_binomial_Coeff_Sum(5), 5)

    def test_even_binomial_Coeff_Sum_negative(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(-1)

    def test_even_binomial_Coeff_Sum_zero(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)

    def test_even_binomial_Coeff_Sum_large(self):
        self.assertEqual(even_binomial_Coeff_Sum(100), 1 << 99)
