import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, larg_nnum, [], 1)

    def test_edge_case_n_zero(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_greater_than_list_length(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3, 4, 5], -1)

    def test_edge_case_non_integer_n(self):
        with self.assertRaises(TypeError):
            larg_nnum([1, 2, 3, 4, 5], 'a')

    def test_edge_case_non_list_input(self):
        with self.assertRaises(TypeError):
            larg_nnum('abc', 1)

    def test_edge_case_non_integer_list_element(self):
        with self.assertRaises(TypeError):
            larg_nnum([1, 2, 'a', 4, 5], 3)
