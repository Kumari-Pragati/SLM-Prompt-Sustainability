import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 3)
        self.assertEqual(even_binomial_Coeff_Sum(5), 5)

    def test_edge(self):
        self.assertEqual(even_binomial_Coeff_Sum(-1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(-2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 3)
        self.assertEqual(even_binomial_Coeff_Sum(5), 5)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum('a')
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(None)
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum([1, 2, 3])
