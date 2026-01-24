import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 1)
        self.assertEqual(even_binomial_Coeff_Sum(3), 2)
        self.assertEqual(even_binomial_Coeff_Sum(4), 2)
        self.assertEqual(even_binomial_Coeff_Sum(5), 4)

    def test_edge_case(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(6), 8)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(3.5)
