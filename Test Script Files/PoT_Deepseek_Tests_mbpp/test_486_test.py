import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0.5), 0.24609375)

    def test_boundary_conditions(self):
        self.assertEqual(binomial_probability(0, 0, 0.5), 1)
        self.assertEqual(binomial_probability(10, 10, 0.5), 0.0009765625)

    def test_edge_cases(self):
        self.assertEqual(binomial_probability(10, 0, 0.5), 0.5 ** 10)
        self.assertEqual(binomial_probability(10, 10, 0.5), 0.5 ** 10)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            binomial_probability(-1, 5, 0.5)
        with self.assertRaises(Exception):
            binomial_probability(10, 11, 0.5)
        with self.assertRaises(Exception):
            binomial_probability(10, 'a', 0.5)
        with self.assertRaises(Exception):
            binomial_probability(10, 5, 1.5)
        with self.assertRaises(Exception):
            binomial_probability(10, 5, -0.5)
