import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(2, 3, 0.5), 5.0)

    def test_single_term(self):
        self.assertAlmostEqual(sum_gp(2, 1, 0.5), 2.0)

    def test_zero_common_ratio(self):
        self.assertAlmostEqual(sum_gp(2, 3, 0), 6.0)

    def test_negative_common_ratio(self):
        self.assertAlmostEqual(sum_gp(2, 3, -0.5), 5.0)

    def test_large_n(self):
        self.assertAlmostEqual(sum_gp(2, 1000, 0.5), 1024.0)

    def test_zero_first_term(self):
        self.assertAlmostEqual(sum_gp(0, 3, 0.5), 0.0)

    def test_large_first_term(self):
        self.assertAlmostEqual(sum_gp(1000, 3, 0.5), 1500.0)

    def test_large_negative_first_term(self):
        self.assertAlmostEqual(sum_gp(-1000, 3, 0.5), -500.0)

    def test_large_negative_common_ratio(self):
        self.assertAlmostEqual(sum_gp(2, 3, -0.999), 5.0)

    def test_large_positive_common_ratio(self):
        self.assertAlmostEqual(sum_gp(2, 3, 0.999), 5.0)

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            sum_gp(2, -3, 0.5)

    def test_invalid_r(self):
        with self.assertRaises(ValueError):
            sum_gp(2, 3, 1)
