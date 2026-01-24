import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 1)
        self.assertEqual(even_binomial_Coeff_Sum(2), 2)
        self.assertEqual(even_binomial_Coeff_Sum(3), 4)
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

    def test_edge_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)

    def test_boundary_cases(self):
        self.assertEqual(even_binomial_Coeff_Sum(5), 16)
        self.assertEqual(even_binomial_Coeff_Sum(6), 32)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum("invalid")
