import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_binomial_probability(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.375, places=3)
        self.assertAlmostEqual(binomial_probability(10, 7, 0.5), 0.021, places=3)
        self.assertAlmostEqual(binomial_probability(5, 2, 0.7), 0.189, places=3)
        self.assertAlmostEqual(binomial_probability(20, 15, 0.3), 0.043, places=3)
        self.assertAlmostEqual(binomial_probability(1, 0, 0.5), 1.0, places=3)
        self.assertAlmostEqual(binomial_probability(1, 1, 0.5), 0.5, places=3)
        self.assertAlmostEqual(binomial_probability(1, 0, 0.0), 1.0, places=3)
        self.assertAlmostEqual(binomial_probability(1, 1, 0.0), 0.0, places=3)
