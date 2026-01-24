import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_binomial_coeff_zero(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(0, 1), 0)

    def test_binomial_coeff_one(self):
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)

    def test_binomial_coeff_small_values(self):
        self.assertEqual(binomial_Coeff(2, 0), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(2, 2), 1)

    def test_binomial_coeff_large_values(self):
        self.assertEqual(binomial_Coeff(10, 0), 1)
        self.assertEqual(binomial_Coeff(10, 1), 10)
        self.assertEqual(binomial_Coeff(10, 2), 45)
        self.assertEqual(binomial_Coeff(10, 5), 252)
