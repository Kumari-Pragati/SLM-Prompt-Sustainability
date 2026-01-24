import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 0), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(2, 2), 1)
        self.assertEqual(binomial_Coeff(3, 0), 1)
        self.assertEqual(binomial_Coeff(3, 1), 3)
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(3, 3), 1)

    def test_edge(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 2), 1)
        self.assertEqual(binomial_Coeff(3, 3), 1)
        self.assertEqual(binomial_Coeff(4, 4), 1)
        self.assertEqual(binomial_Coeff(5, 5), 1)
        self.assertEqual(binomial_Coeff(10, 10), 1)
        self.assertEqual(binomial_Coeff(10, 0), 1)
        self.assertEqual(binomial_Coeff(10, 1), 10)
        self.assertEqual(binomial_Coeff(10, 2), 45)
        self.assertEqual(binomial_Coeff(10, 3), 120)
        self.assertEqual(binomial_Coeff(10, 4), 210)
        self.assertEqual(binomial_Coeff(10, 5), 252)
        self.assertEqual(binomial_Coeff(10, 6), 210)
        self.assertEqual(binomial_Coeff(10, 7), 120)
        self.assertEqual(binomial_Coeff(10, 8), 45)
        self.assertEqual(binomial_Coeff(10, 9), 10)
        self.assertEqual(binomial_Coeff(10, 10), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(-1, 0)
        with self.assertRaises(TypeError):
            binomial_Coeff(0, -1)
        with self.assertRaises(TypeError):
            binomial_Coeff(-1, -1)
        with self.assertRaises(TypeError):
            binomial_Coeff(-1, 1)
        with self.assertRaises(TypeError):
            binomial_Coeff(1, -1)
        with self.assertRaises(TypeError):
            binomial_Coeff(1, 1)
