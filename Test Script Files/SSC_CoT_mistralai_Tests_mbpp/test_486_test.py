import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0.5), 0.6241509463564878)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.5), 0.2480162466758892)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(1, 1, 0), 0)
        self.assertAlmostEqual(binomial_probability(1, 0, 0), 1)
        self.assertAlmostEqual(binomial_probability(1, 1, 1), 0)
        self.assertAlmostEqual(binomial_probability(1, 0, 1), 0)
        self.assertAlmostEqual(binomial_probability(10, 11, 0.5), 0)
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 0)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            binomial_probability(-1, 1, 0.5)
        with self.assertRaises(ValueError):
            binomial_probability(1, -1, 0.5)
        with self.assertRaises(ValueError):
            binomial_probability(1, 1, -0.5)
