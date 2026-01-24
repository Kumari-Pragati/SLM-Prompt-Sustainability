import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binomial_Coeff(4, 2), 6)
        self.assertEqual(binomial_Coeff(5, 3), 10)
        self.assertEqual(binomial_Coeff(6, 4), 15)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 2), 1)
        self.assertEqual(binomial_Coeff(3, 3), 1)
        self.assertEqual(binomial_Coeff(4, 4), 1)
        self.assertEqual(binomial_Coeff(5, 5), 1)
        self.assertEqual(binomial_Coeff(6, 6), 1)
        self.assertEqual(binomial_Coeff(7, 7), 1)

        self.assertEqual(binomial_Coeff(0, 1), 0)
        self.assertEqual(binomial_Coeff(1, 2), 0)
        self.assertEqual(binomial_Coeff(2, 3), 0)
        self.assertEqual(binomial_Coeff(3, 4), 0)
        self.assertEqual(binomial_Coeff(4, 5), 0)
        self.assertEqual(binomial_Coeff(5, 6), 0)
        self.assertEqual(binomial_Coeff(6, 7), 0)
