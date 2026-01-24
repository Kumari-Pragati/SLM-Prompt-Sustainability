import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 4)
        self.assertEqual(even_binomial_Coeff_Sum(5), 5)
        self.assertEqual(even_binomial_Coeff_Sum(6), 6)
        self.assertEqual(even_binomial_Coeff_Sum(7), 7)
        self.assertEqual(even_binomial_Coeff_Sum(8), 8)
        self.assertEqual(even_binomial_Coeff_Sum(9), 9)
        self.assertEqual(even_binomial_Coeff_Sum(10), 10)

    def test_even_binomial_Coeff_Sum_edge_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 0)
        self.assertEqual(even_binomial_Coeff_Sum(-1), 0)

    def test_even_binomial_Coeff_Sum_invalid_input(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum('a')
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(None)
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(1.5)
