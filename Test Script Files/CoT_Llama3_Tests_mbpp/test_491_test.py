import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(100, 10, 0.1), 550.0)

    def test_edge_case_r_zero(self):
        self.assertAlmostEqual(sum_gp(100, 10, 0), 1000.0)

    def test_edge_case_r_one(self):
        self.assertAlmostEqual(sum_gp(100, 10, 1), 100.0)

    def test_edge_case_n_zero(self):
        self.assertAlmostEqual(sum_gp(100, 0, 0.1), 100.0)

    def test_invalid_input_non_numeric_a(self):
        with self.assertRaises(TypeError):
            sum_gp('a', 10, 0.1)

    def test_invalid_input_non_numeric_r(self):
        with self.assertRaises(TypeError):
            sum_gp(100, 10, 'r')

    def test_invalid_input_non_numeric_n(self):
        with self.assertRaises(TypeError):
            sum_gp(100, 'n', 0.1)
