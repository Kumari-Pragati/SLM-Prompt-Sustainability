import unittest
from mbpp_274_code import even_binomial_Coeff_Sum

class TestEvenBinomialCoeffSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_binomial_Coeff_Sum(5), 16)

    def test_boundary_case_zero(self):
        self.assertEqual(even_binomial_Coeff_Sum(0), 1)

    def test_boundary_case_one(self):
        self.assertEqual(even_binomial_Coeff_Sum(1), 2)

    def test_large_number(self):
        self.assertEqual(even_binomial_Coeff_Sum(20), 1048576)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            even_binomial_Coeff_Sum(-5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            even_binomial_Coeff_Sum(5.5)
