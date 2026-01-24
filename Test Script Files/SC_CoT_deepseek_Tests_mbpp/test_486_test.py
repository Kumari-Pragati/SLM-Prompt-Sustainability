import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0.5), 0.24609375)

    def test_boundary_case(self):
        self.assertAlmostEqual(binomial_probability(0, 0, 0.5), 1)
        self.assertAlmostEqual(binomial_probability(10, 10, 0.5), 0.0009765625)

    def test_edge_case(self):
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 0.0009765625)
        self.assertAlmostEqual(binomial_probability(10, 10, 0.5), 0.0009765625)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            binomial_probability("10", 5, 0.5)
        with self.assertRaises(TypeError):
            binomial_probability(10, "5", 0.5)
        with self.assertRaises(TypeError):
            binomial_probability(10, 5, "0.5")
        with self.assertRaises(ValueError):
            binomial_probability(10, 11, 0.5)
        with self.assertRaises(ValueError):
            binomial_probability(10, -1, 0.5)
        with self.assertRaises(ValueError):
            binomial_probability(10, 5, -1)
        with self.assertRaises(ValueError):
            binomial_probability(10, 5, 1.5)
