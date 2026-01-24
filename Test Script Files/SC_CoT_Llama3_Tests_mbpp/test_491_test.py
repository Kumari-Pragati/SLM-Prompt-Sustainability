import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_gp(10, 5, 0.5), 14.375)

    def test_edge_case_n_zero(self):
        self.assertRaises(ZeroDivisionError, sum_gp, 10, 0, 0.5)

    def test_edge_case_r_one(self):
        self.assertEqual(sum_gp(10, 5, 1), 10)

    def test_edge_case_a_zero(self):
        self.assertEqual(sum_gp(0, 5, 0.5), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(sum_gp(10, 1, 0.5), 10)

    def test_invalid_input_non_numeric_a(self):
        with self.assertRaises(TypeError):
            sum_gp('ten', 5, 0.5)

    def test_invalid_input_non_numeric_n(self):
        with self.assertRaises(TypeError):
            sum_gp(10, 'five', 0.5)

    def test_invalid_input_non_numeric_r(self):
        with self.assertRaises(TypeError):
            sum_gp(10, 5, 'half')

    def test_edge_case_r_zero(self):
        self.assertRaises(ZeroDivisionError, sum_gp, 10, 5, 0)

    def test_edge_case_n_negative(self):
        self.assertRaises(ValueError, sum_gp, 10, -5, 0.5)

    def test_edge_case_r_negative(self):
        self.assertRaises(ValueError, sum_gp, 10, 5, -0.5)
