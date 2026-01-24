import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_binomial_probability(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.375)
        self.assertAlmostEqual(binomial_probability(10, 5, 0.5), 0.03125)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.5), 0.1171875)
        self.assertAlmostEqual(binomial_probability(5, 2, 0.5), 0.375)
        self.assertAlmostEqual(binomial_probability(1, 0, 0.5), 1.0)
        self.assertAlmostEqual(binomial_probability(1, 1, 0.5), 0.5)
        self.assertAlmostEqual(binomial_probability(0, 0, 0.5), 1.0)
        self.assertAlmostEqual(binomial_probability(0, 1, 0.5), 0.0)
        self.assertAlmostEqual(binomial_probability(10, 11, 0.5), 0.0)
        self.assertAlmostEqual(binomial_probability(10, -1, 0.5), 0.0)
        self.assertAlmostEqual(binomial_probability(-10, 3, 0.5), 0.0)
        self.assertAlmostEqual(binomial_probability(10, 3, 1.0), 0.5)
        self.assertAlmostEqual(binomial_probability(10, 3, 0.0), 0.0)
        self.assertAlmostEqual(binomial_probability(10, 3, -1.0), 0.0)
