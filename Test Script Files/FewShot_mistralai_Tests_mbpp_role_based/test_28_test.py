import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(1, 2), 0)
        self.assertEqual(binomial_Coeff(2, 2), 1)
        self.assertEqual(binomial_Coeff(2, 3), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 1)
        self.assertRaises(ValueError, binomial_Coeff, 1, -1)
        self.assertRaises(ValueError, binomial_Coeff, 0, 0)
