import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_empty_list(self):
        self.assertEqual(larg_nnum([], 1), [])

    def test_edge_case_single_element(self):
        self.assertEqual(larg_nnum([1], 1), [1])

    def test_edge_case_single_element_largest(self):
        self.assertEqual(larg_nnum([-1], 1), [-1])

    def test_edge_case_n_larger_than_list_length(self):
        self.assertEqual(larg_nnum([1, 2, 3], 4), [1, 2, 3])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(larg_nnum([-1, -2, -3], 2), [-3, -2])
