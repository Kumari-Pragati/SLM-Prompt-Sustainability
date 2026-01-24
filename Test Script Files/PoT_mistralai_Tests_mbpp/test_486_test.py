import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.2431957627)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.5), 0.078125)

    def test_edge_cases(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(0, 1, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 0, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 1, 1), 0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(binomial_probability(2, 1, 0), 0)
        self.assertAlmostEqual(binomial_probability(2, 2, 0), 1)
        self.assertAlmostEqual(binomial_probability(2, 0, 0), 0)
        self.assertAlmostEqual(binomial_probability(2, 2, 1), 0)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, binomial_probability, -1, 2, 0.5)
        self.assertRaises(ValueError, binomial_probability, 0, -1, 0.5)
        self.assertRaises(ValueError, binomial_probability, 2, -1, 0.5)
