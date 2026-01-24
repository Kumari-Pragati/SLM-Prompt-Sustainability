import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 7)
        self.assertEqual(even_binomial_Coeff_Sum(5), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_binomial_Coeff_Sum(-1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(3), 3)
        self.assertEqual(even_binomial_Coeff_Sum(4), 7)
        self.assertEqual(even_binomial_Coeff_Sum(5), 15)

    def test_special_and_corner_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(6), 31)
        self.assertEqual(even_binomial_Coeff_Sum(7), 63)
        self.assertEqual(even_binomial_Coeff_Sum(8), 127)
        self.assertEqual(even_binomial_Coeff_Sum(9), 255)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum('a')
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(None)
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum([1, 2, 3])
