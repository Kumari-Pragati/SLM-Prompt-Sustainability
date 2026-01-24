import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.125, places=3)

    def test_edge_case_p_zero(self):
        self.assertEqual(binomial_probability(10, 3, 0), 0)

    def test_edge_case_p_one(self):
        self.assertEqual(binomial_probability(10, 3, 1), 0)

    def test_edge_case_k_zero(self):
        self.assertEqual(binomial_probability(10, 0, 0.5), 0)

    def test_edge_case_k_n(self):
        self.assertEqual(binomial_probability(10, 10, 0.5), 0.5)

    def test_edge_case_n_zero(self):
        with self.assertRaises(ZeroDivisionError):
            binomial_probability(0, 3, 0.5)

    def test_edge_case_r_greater_than_n_half(self):
        self.assertAlmostEqual(binomial_probability(10, 7, 0.5), binomial_probability(10, 3, 0.5), places=3)

    def test_edge_case_p_greater_than_one(self):
        with self.assertRaises(OverflowError):
            binomial_probability(10, 3, 1.1)

    def test_edge_case_p_less_than_zero(self):
        with self.assertRaises(OverflowError):
            binomial_probability(10, 3, -0.1)
