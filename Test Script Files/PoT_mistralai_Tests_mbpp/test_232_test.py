import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertListEqual(larg_nnum([10, 20, 30, 40, 50], 2), [50, 40])
        self.assertListEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-5, -4, -3])

    def test_edge_case_empty_list(self):
        self.assertListEqual(larg_nnum([], 2), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(larg_nnum([1], 1), [1])

    def test_edge_case_single_element_negative(self):
        self.assertListEqual(larg_nnum([-1], 1), [-1])

    def test_edge_case_n_greater_than_len(self):
        self.assertListEqual(larg_nnum([1, 2, 3], 5), [1, 2, 3])

    def test_edge_case_n_less_than_zero(self):
        self.assertListEqual(larg_nnum([1, 2, 3], -1), [3, 2, 1])
