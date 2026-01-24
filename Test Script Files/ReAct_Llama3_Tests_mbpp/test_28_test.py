import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_zero_or_n(self):
        self.assertEqual(binomial_Coeff(5,0), 1)
        self.assertEqual(binomial_Coeff(5,5), 1)

    def test_k_greater_than_n(self):
        self.assertEqual(binomial_Coeff(5,6), 0)

    def test_k_and_n_equal(self):
        self.assertEqual(binomial_Coeff(5,1), 5)

    def test_k_and_n_greater_than_1(self):
        self.assertEqual(binomial_Coeff(5,2), 10)

    def test_recursive_calls(self):
        self.assertEqual(binomial_Coeff(10,3), 45)
