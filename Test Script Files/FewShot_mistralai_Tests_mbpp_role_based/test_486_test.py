import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.44721359549937)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.5), 0.078125)

    def test_zero_n(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0.5), 1.0)

    def test_negative_n(self):
        self.assertRaises(ValueError, binomial_probability, -1, 0, 0.5)

    def test_negative_k(self):
        self.assertRaises(ValueError, binomial_probability, 10, -1, 0.5)

    def test_negative_p(self):
        self.assertRaises(ValueError, binomial_probability, 10, 5, -0.5)

    def test_invalid_p(self):
        self.assertRaises(ValueError, binomial_probability, 10, 5, 1.1)
