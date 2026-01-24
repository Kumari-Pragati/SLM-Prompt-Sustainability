import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_simple(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.14050909)
        self.assertAlmostEqual(binomial_probability(5, 2, 0.7), 0.38461538)

    def test_edge_cases(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(1, 1, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(1, 1, 1), 0)

        self.assertAlmostEqual(binomial_probability(100, 100, 0.5), 0.0)
        self.assertAlmostEqual(binomial_probability(100, 0, 0.5), 1)

    def test_boundary(self):
        self.assertAlmostEqual(binomial_probability(10, 11, 0.5), 0)
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 1)
        self.assertAlmostEqual(binomial_probability(10, 10, 0), 1)
        self.assertAlmostEqual(binomial_probability(10, 10, 1), 0)
