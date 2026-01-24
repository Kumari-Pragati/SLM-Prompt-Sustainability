import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_sum_gp_positive_numbers(self):
        self.assertAlmostEqual(sum_gp(1, 3, 0.5), 4.0)

    def test_sum_gp_negative_numbers(self):
        self.assertAlmostEqual(sum_gp(-1, 3, -0.5), -4.0)

    def test_sum_gp_zero_common_ratio(self):
        self.assertEqual(sum_gp(1, 3, 0), 1)

    def test_sum_gp_single_term(self):
        self.assertEqual(sum_gp(1, 1, 0.5), 1)

    def test_sum_gp_zero_first_term(self):
        self.assertEqual(sum_gp(0, 3, 0.5), 0)

    def test_sum_gp_large_numbers(self):
        self.assertAlmostEqual(sum_gp(1000, 10, 0.1), 161051.0)
