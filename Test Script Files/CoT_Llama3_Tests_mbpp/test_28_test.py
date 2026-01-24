import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_binomial_coeff_valid(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(4, 0), 1)
        self.assertEqual(binomial_Coeff(4, 1), 4)
        self.assertEqual(binomial_Coeff(4, 2), 6)
        self.assertEqual(binomial_Coeff(4, 3), 4)
        self.assertEqual(binomial_Coeff(4, 4), 1)

    def test_binomial_coeff_invalid(self):
        with self.assertRaises(TypeError):
            binomial_Coeff('a', 2)
        with self.assertRaises(TypeError):
            binomial_Coeff(5, 'b')
        with self.assertRaises(TypeError):
            binomial_Coeff('a', 'b')

    def test_binomial_coeff_edge(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 0), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(2, 2), 1)

    def test_binomial_coeff_k_greater_than_n(self):
        self.assertEqual(binomial_Coeff(5, 6), 0)
