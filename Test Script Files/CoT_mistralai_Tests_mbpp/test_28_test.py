import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(0, 1), 0)

    def test_one(self):
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)

    def test_positive_numbers(self):
        self.assertEqual(binomial_Coeff(5, 3), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)

    def test_k_greater_than_n(self):
        self.assertEqual(binomial_Coeff(3, 4), 0)
        self.assertEqual(binomial_Coeff(5, 6), 0)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 1)
        self.assertRaises(ValueError, binomial_Coeff, 1, -1)

    def test_floating_point_inputs(self):
        self.assertEqual(binomial_Coeff(5, 2.5), 0)
        self.assertEqual(binomial_Coeff(2.5, 1), 2.5)
