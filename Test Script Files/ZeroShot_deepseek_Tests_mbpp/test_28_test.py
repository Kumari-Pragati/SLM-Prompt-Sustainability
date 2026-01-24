import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_binomial_Coeff_basic(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)

    def test_binomial_Coeff_zero(self):
        self.assertEqual(binomial_Coeff(5, 0), 1)

    def test_binomial_Coeff_same(self):
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_binomial_Coeff_greater(self):
        self.assertEqual(binomial_Coeff(5, 6), 0)

    def test_binomial_Coeff_negative(self):
        self.assertEqual(binomial_Coeff(-5, 2), 0)

    def test_binomial_Coeff_float(self):
        self.assertEqual(binomial_Coeff(5.5, 2), None)
