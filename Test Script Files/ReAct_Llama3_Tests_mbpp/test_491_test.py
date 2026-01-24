import unittest
from mbpp_491_code import sum_gp

class TestSumGp(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(100, 10, 0.1), 5499.5, places=1)

    def test_edge_case_r_zero(self):
        self.assertAlmostEqual(sum_gp(100, 10, 0), 10000, places=1)

    def test_edge_case_n_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sum_gp(100, 0, 0.1)

    def test_edge_case_r_one(self):
        with self.assertRaises(ZeroDivisionError):
            sum_gp(100, 10, 1)

    def test_edge_case_a_zero(self):
        self.assertAlmostEqual(sum_gp(0, 10, 0.1), 0, places=1)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            sum_gp(100, -10, 0.1)

    def test_edge_case_r_negative(self):
        with self.assertRaises(ValueError):
            sum_gp(100, 10, -0.1)
