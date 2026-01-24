import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)

    def test_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(5, 0), 1)
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_edge_cases(self):
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            binomial_Coeff(-1, 2)
        with self.assertRaises(Exception):
            binomial_Coeff(2, -1)
        with self.assertRaises(Exception):
            binomial_Coeff(2, 3)
