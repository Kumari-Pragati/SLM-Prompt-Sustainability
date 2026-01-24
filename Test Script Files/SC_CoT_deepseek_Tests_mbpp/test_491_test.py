import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(1, 5, 0.5), 4.0)

    def test_edge_case_n_equals_1(self):
        self.assertAlmostEqual(sum_gp(1, 1, 0.5), 1.0)

    def test_edge_case_r_equals_1(self):
        self.assertAlmostEqual(sum_gp(1, 5, 1), 5.0)

    def test_edge_case_r_equals_0(self):
        self.assertAlmostEqual(sum_gp(1, 5, 0), 1.0)

    def test_invalid_input_n_less_than_0(self):
        with self.assertRaises(ValueError):
            sum_gp(1, -1, 0.5)

    def test_invalid_input_r_equals_1_and_n_greater_than_0(self):
        with self.assertRaises(ValueError):
            sum_gp(1, 1, 1)
