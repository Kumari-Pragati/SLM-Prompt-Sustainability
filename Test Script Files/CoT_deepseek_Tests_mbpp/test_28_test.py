import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binomial_Coeff(5, 2), 10)
        self.assertEqual(binomial_Coeff(10, 5), 252)
        self.assertEqual(binomial_Coeff(15, 10), 3003)

    def test_boundary_conditions(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(5, 0), 1)
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            binomial_Coeff(1000, 500)
        with self.assertRaises(TypeError):
            binomial_Coeff("5", 2)
        with self.assertRaises(TypeError):
            binomial_Coeff(5, "2")
        with self.assertRaises(TypeError):
            binomial_Coeff("5", "2")
