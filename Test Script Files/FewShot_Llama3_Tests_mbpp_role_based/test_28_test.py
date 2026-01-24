import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)

    def test_edge_case_k_zero(self):
        self.assertEqual(binomial_Coeff(5, 0), 1)

    def test_edge_case_k_equal_n(self):
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(binomial_Coeff(5, 6), 0)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(-5, 2)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(5, -2)
