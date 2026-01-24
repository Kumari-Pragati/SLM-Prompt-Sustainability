import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(4), 6)
        self.assertEqual(even_binomial_Coeff_Sum(6), 14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 0)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(5), 10)
        self.assertEqual(even_binomial_Coeff_Sum(7), 30)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 'string')
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, -1)
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 0.5)
