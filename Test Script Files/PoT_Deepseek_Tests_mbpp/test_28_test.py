import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)
        self.assertEqual(binomial_Coeff(15, 8), 6435)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(10, 0), 1)
        self.assertEqual(binomial_Coeff(10, 10), 1)
        self.assertEqual(binomial_Coeff(10, 10), 1)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(Exception):
            binomial_Coeff(-5, 2)
        with self.assertRaises(Exception):
            binomial_Coeff(5, -2)
        with self.assertRaises(Exception):
            binomial_Coeff(5, 6)
