import unittest
from mbpp_912_code import binomial_coeff, lobb_num

class TestBinomialCoeff(unittest.TestCase):
    def test_binomial_coeff_basic(self):
        self.assertEqual(binomial_coeff(2, 0), 1)
        self.assertEqual(binomial_coeff(2, 1), 2)
        self.assertEqual(binomial_coeff(2, 2), 2)
        self.assertEqual(binomial_coeff(3, 0), 1)
        self.assertEqual(binomial_coeff(3, 1), 3)
        self.assertEqual(binomial_coeff(3, 2), 3)
        self.assertEqual(binomial_coeff(3, 3), 1)

    def test_binomial_coeff_large_input(self):
        self.assertEqual(binomial_coeff(10, 5), 252)
        self.assertEqual(binomial_coeff(20, 10), 184756)

class TestLobbNum(unittest.TestCase):
    def test_lobb_num_basic(self):
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 2), 9)
        self.assertEqual(lobb_num(3, 3), 36)

    def test_lobb_num_large_input(self):
        self.assertEqual(lobb_num(10, 20), 138789820)
        self.assertEqual(lobb_num(20, 40), 1214460607740)
