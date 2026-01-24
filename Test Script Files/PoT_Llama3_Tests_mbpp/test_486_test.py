import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.125)

    def test_edge_case_p_zero(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.0), 0.0)

    def test_edge_case_p_one(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 1.0), 1.0)

    def test_edge_case_k_zero(self):
        self.assertAlmostEqual(binomial_probability(10, 0, 0.5), 0.0)

    def test_edge_case_k_n(self):
        self.assertAlmostEqual(binomial_probability(10, 10, 0.5), 0.0)

    def test_edge_case_n_zero(self):
        self.assertAlmostEqual(binomial_probability(0, 3, 0.5), 0.0)

    def test_edge_case_invalid_p(self):
        with self.assertRaises(ValueError):
            binomial_probability(10, 3, -0.5)

    def test_edge_case_invalid_k(self):
        with self.assertRaises(ValueError):
            binomial_probability(10, -3, 0.5)

    def test_edge_case_invalid_n(self):
        with self.assertRaises(ValueError):
            binomial_probability(-10, 3, 0.5)
