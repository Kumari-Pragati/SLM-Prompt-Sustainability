import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(binomial_probability(10, 3, 0.5), 0.125)

    def test_edge_case_p_zero(self):
        self.assertEqual(binomial_probability(10, 3, 0), 0)

    def test_edge_case_p_one(self):
        self.assertEqual(binomial_probability(10, 3, 1), 0)

    def test_edge_case_k_zero(self):
        self.assertEqual(binomial_probability(10, 0, 0.5), 0.5 ** 10)

    def test_edge_case_k_n(self):
        self.assertEqual(binomial_probability(10, 10, 0.5), 0.5 ** 10)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(TypeError):
            binomial_probability(-1, 3, 0.5)

    def test_invalid_input_k_negative(self):
        with self.assertRaises(TypeError):
            binomial_probability(10, -1, 0.5)

    def test_invalid_input_p_out_of_range(self):
        with self.assertRaises(TypeError):
            binomial_probability(10, 3, 2)
