import unittest
from mbpp_28_code import binomial_Coeff

class TestBinomialCoeff(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(binomial_Coeff(5,2), 10)

    def test_edge1(self):
        self.assertEqual(binomial_Coeff(5,0), 1)

    def test_edge2(self):
        self.assertEqual(binomial_Coeff(5,5), 1)

    def test_edge3(self):
        self.assertEqual(binomial_Coeff(5,6), 0)

    def test_edge4(self):
        self.assertEqual(binomial_Coeff(0,2), 0)

    def test_edge5(self):
        self.assertEqual(binomial_Coeff(2,0), 1)

    def test_edge6(self):
        self.assertEqual(binomial_Coeff(2,2), 1)

    def test_edge7(self):
        self.assertEqual(binomial_Coeff(2,3), 1)

    def test_edge8(self):
        self.assertEqual(binomial_Coeff(2,4), 1)

    def test_edge9(self):
        self.assertEqual(binomial_Coeff(2,5), 0)

    def test_edge10(self):
        self.assertEqual(binomial_Coeff(2,6), 0)

    def test_invalid1(self):
        with self.assertRaises(TypeError):
            binomial_Coeff('a', 2)

    def test_invalid2(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(2, 'b')

    def test_invalid3(self):
        with self.assertRaises(TypeError):
            binomial_Coeff('a', 'b')
