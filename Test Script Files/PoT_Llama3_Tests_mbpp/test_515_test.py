import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))

    def test_edge_case_n_eq_m(self):
        self.assertTrue(modular_sum([1, 2, 3], 5, 5))

    def test_edge_case_n_lt_m(self):
        self.assertFalse(modular_sum([1, 2, 3], 2, 5))

    def test_edge_case_arr_empty(self):
        self.assertFalse(modular_sum([], 3, 5))

    def test_edge_case_n_eq_0(self):
        self.assertFalse(modular_sum([], 0, 5))

    def test_edge_case_m_eq_0(self):
        with self.assertRaises(IndexError):
            modular_sum([1, 2, 3], 3, 0)

    def test_edge_case_m_eq_1(self):
        self.assertFalse(modular_sum([1, 2, 3], 3, 1))

    def test_edge_case_arr_single(self):
        self.assertFalse(modular_sum([1], 1, 5))

    def test_edge_case_arr_single_n_eq_m(self):
        self.assertTrue(modular_sum([1], 1, 1))

    def test_edge_case_arr_single_n_lt_m(self):
        self.assertFalse(modular_sum([1], 0, 5))

    def test_edge_case_arr_single_m_eq_0(self):
        with self.assertRaises(IndexError):
            modular_sum([1], 1, 0)

    def test_edge_case_arr_single_m_eq_1(self):
        self.assertFalse(modular_sum([1], 1, 1))
