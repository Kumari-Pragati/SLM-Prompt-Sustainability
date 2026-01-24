import unittest
from mbpp_486_code import binomial_probability

class TestBinomialProbability(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(binomial_probability(10, 5, 0.5), 0.24609375, places=6)

    def test_boundary_case_n_equals_k(self):
        self.assertAlmostEqual(binomial_probability(5, 5, 0.5), 0.03125, places=6)

    def test_boundary_case_p_equals_0(self):
        self.assertEqual(binomial_probability(10, 5, 0), 0)

    def test_boundary_case_p_equals_1(self):
        self.assertEqual(binomial_probability(10, 5, 1), 0)

    def test_boundary_case_n_equals_0(self):
        self.assertEqual(binomial_probability(0, 5, 0.5), 0)

    def test_boundary_case_k_equals_0(self):
        self.assertEqual(binomial_probability(10, 0, 0.5), 1)

    def test_boundary_case_k_equals_n(self):
        self.assertAlmostEqual(binomial_probability(5, 5, 0.5), 0.03125, places=6)

    def test_error_case_negative_n(self):
        with self.assertRaises(Exception):
            binomial_probability(-5, 2, 0.5)

    def test_error_case_negative_k(self):
        with self.assertRaises(Exception):
            binomial_probability(5, -2, 0.5)

    def test_error_case_negative_p(self):
        with self.assertRaises(Exception):
            binomial_probability(5, 2, -0.5)

    def test_error_case_negative_p_greater_than_1(self):
        with self.assertRaises(Exception):
            binomial_probability(5, 2, 1.5)

    def test_error_case_n_not_integer(self):
        with self.assertRaises(Exception):
            binomial_probability(5.5, 2, 0.5)

    def test_error_case_k_not_integer(self):
        with self.assertRaises(Exception):
            binomial_probability(5, 2.2, 0.5)

    def test_error_case_p_not_float(self):
        with self.assertRaises(Exception):
            binomial_probability(5, 2, 'a')
