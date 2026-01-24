import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(sum_gp(100, 5, 0.05), 161.01010101010102)

    def test_edge_case_zero_rate(self):
        self.assertAlmostEqual(sum_gp(100, 5, 0), 500)

    def test_edge_case_zero_n(self):
        self.assertAlmostEqual(sum_gp(100, 0, 0.05), 100)

    def test_edge_case_zero_a(self):
        self.assertAlmostEqual(sum_gp(0, 5, 0.05), 0)

    def test_invalid_input_non_numeric_a(self):
        with self.assertRaises(TypeError):
            sum_gp('a', 5, 0.05)

    def test_invalid_input_non_numeric_n(self):
        with self.assertRaises(TypeError):
            sum_gp(100, 'n', 0.05)

    def test_invalid_input_non_numeric_r(self):
        with self.assertRaises(TypeError):
            sum_gp(100, 5, 'r')
