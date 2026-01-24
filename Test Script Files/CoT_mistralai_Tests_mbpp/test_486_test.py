import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.4472135954999578)
        self.assertAlmostEqual(binomial_probability(20, 10, 0.5), 0.078125)

    def test_edge_case_small_n(self):
        self.assertAlmostEqual(binomial_probability(2, 1, 0.5), 0.5)
        self.assertAlmostEqual(binomial_probability(2, 2, 0.5), 0.25)

    def test_edge_case_large_n(self):
        self.assertAlmostEqual(binomial_probability(100, 50, 0.5), 0.0778783078125)
        self.assertAlmostEqual(binomial_probability(100, 99, 0.5), 0.0001220703125)

    def test_edge_case_p_0(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0), 0)
        self.assertAlmostEqual(binomial_probability(10, 1, 0), 0)

    def test_edge_case_p_1(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 1), 0)
        self.assertAlmostEqual(binomial_probability(10, 1, 1), 1)

    def test_invalid_input_n(self):
        self.assertRaises(ValueError, binomial_probability, -1, 1, 0.5)
        self.assertRaises(ValueError, binomial_probability, 0, 1, 0.5)

    def test_invalid_input_k(self):
        self.assertRaises(ValueError, binomial_probability, 10, -1, 0.5)
        self.assertRaises(ValueError, binomial_probability, 10, 11, 0.5)

    def test_invalid_input_p(self):
        self.assertRaises(ValueError, binomial_probability, 10, 5, -1)
        self.assertRaises(ValueError, binomial_probability, 10, 5, 1.1)
