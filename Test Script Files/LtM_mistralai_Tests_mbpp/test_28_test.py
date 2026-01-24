import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(binomial_Coeff(4, 2), 6)
        self.assertEqual(binomial_Coeff(5, 3), 10)
        self.assertEqual(binomial_Coeff(6, 4), 15)

    def test_edge_and_boundary(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(1, 2), 0)
        self.assertEqual(binomial_Coeff(2, 2), 1)
        self.assertEqual(binomial_Coeff(2, 3), 0)
        self.assertEqual(binomial_Coeff(3, 3), 1)
        self.assertEqual(binomial_Coeff(4, 4), 1)
        self.assertEqual(binomial_Coeff(4, 5), 0)

    def test_negative_or_zero_inputs(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 2)
        self.assertRaises(ValueError, binomial_Coeff, 0, -1)
        self.assertRaises(ValueError, binomial_Coeff, 0, 0)

    def test_k_greater_than_n(self):
        self.assertEqual(binomial_Coeff(3, 4), 0)
        self.assertEqual(binomial_Coeff(4, 5), 0)
        self.assertEqual(binomial_Coeff(5, 6), 0)
