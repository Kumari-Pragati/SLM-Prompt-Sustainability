import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.447213595499958), "Typical case not working correctly"

    def test_edge_case_zero_k(self):
        self.assertAlmostEqual(binomial_probability(5, 0, 0.5), 1, "Edge case with k=0 not working correctly")

    def test_edge_case_zero_p(self):
        self.assertAlmostEqual(binomial_probability(5, 3, 0), 0, "Edge case with p=0 not working correctly")

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            binomial_probability(-5, 3, 0.5), "Edge case with negative n not raising ValueError"

    def test_edge_case_negative_k(self):
        with self.assertRaises(ValueError):
            binomial_probability(5, -3, 0.5), "Edge case with negative k not raising ValueError"

    def test_edge_case_negative_p(self):
        with self.assertRaises(ValueError):
            binomial_probability(5, 3, -0.5), "Edge case with negative p not raising ValueError"

    def test_edge_case_non_integer_n(self):
        with self.assertRaises(TypeError):
            binomial_probability(5.5, 3, 0.5), "Edge case with non-integer n not raising TypeError"

    def test_edge_case_non_integer_k(self):
        with self.assertRaises(TypeError):
            binomial_probability(5, 3.5, 0.5), "Edge case with non-integer k not raising TypeError"

    def test_edge_case_non_number_p(self):
        with self.assertRaises(TypeError):
            binomial_probability(5, 3, "not a number"), "Edge case with non-number p not raising TypeError"
