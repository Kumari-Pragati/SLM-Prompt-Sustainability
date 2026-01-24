import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(1, 3, 0.5), 4.0)

    def test_edge_case_with_zero_common_ratio(self):
        self.assertAlmostEqual(sum_gp(1, 3, 0), 1.0)

    def test_edge_case_with_single_term(self):
        self.assertAlmostEqual(sum_gp(1, 1, 0.5), 1.0)

    def test_edge_case_with_infinite_common_ratio(self):
        with self.assertRaises(ZeroDivisionError):
            sum_gp(1, 3, 1)

    def test_negative_common_ratio(self):
        self.assertAlmostEqual(sum_gp(1, 3, -0.5), 4.0)

    def test_negative_first_term(self):
        self.assertAlmostEqual(sum_gp(-1, 3, 0.5), -4.0)

    def test_negative_number_of_terms(self):
        with self.assertRaises(ValueError):
            sum_gp(1, -3, 0.5)

    def test_zero_first_term(self):
        self.assertAlmostEqual(sum_gp(0, 3, 0.5), 0.0)

    def test_large_number_of_terms(self):
        self.assertAlmostEqual(sum_gp(1, 1000, 0.5), 1.2676506002282294e+200)
