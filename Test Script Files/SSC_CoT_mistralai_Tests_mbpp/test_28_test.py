import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)
        self.assertEqual(binomial_Coeff(20, 10), 1974306327351714)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 0)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(1, 2), 0)
        self.assertEqual(binomial_Coeff(2, 2), 1)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 1)
        self.assertRaises(ValueError, binomial_Coeff, 1, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, binomial_Coeff, 0, 0)
