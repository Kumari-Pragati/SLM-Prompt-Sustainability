import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(even_binomial_Coeff_Sum(2), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 15)
        self.assertEqual(even_binomial_Coeff_Sum(6), 105)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(5), 45)
        self.assertEqual(even_binomial_Coeff_Sum(10), 945)

    def test_negative_input(self):
        self.assertRaises(ValueError, even_binomial_Coeff_Sum, -1)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, even_binomial_Coeff_Sum, 2.5)
