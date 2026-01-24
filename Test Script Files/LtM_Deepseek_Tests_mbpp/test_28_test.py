import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)

    def test_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(5, 0), 1)
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_edge_cases(self):
        self.assertEqual(binomial_Coeff(5, 6), 0)
        self.assertEqual(binomial_Coeff(5, -1), 0)
        self.assertEqual(binomial_Coeff(-5, 2), 0)
        self.assertEqual(binomial_Coeff(-5, -2), 0)
