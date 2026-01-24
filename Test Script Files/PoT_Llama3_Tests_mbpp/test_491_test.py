import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(10, 5, 0.5), 24.0)

    def test_edge_case_zero_rate(self):
        self.assertAlmostEqual(sum_gp(10, 5, 0), 50.0)

    def test_edge_case_zero_n(self):
        self.assertAlmostEqual(sum_gp(10, 0, 0.5), 10.0)

    def test_edge_case_zero_a(self):
        self.assertAlmostEqual(sum_gp(0, 5, 0.5), 0.0)

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            sum_gp(10, -5, 0.5)

    def test_edge_case_negative_a(self):
        with self.assertRaises(ValueError):
            sum_gp(-10, 5, 0.5)

    def test_edge_case_negative_rate(self):
        with self.assertRaises(ValueError):
            sum_gp(10, 5, -0.5)

    def test_edge_case_n_greater_than_a(self):
        with self.assertRaises(ValueError):
            sum_gp(10, 15, 0.5)

    def test_edge_case_rate_greater_than_one(self):
        with self.assertRaises(ValueError):
            sum_gp(10, 5, 1.5)
