import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_n_equal_to_list_length(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case_n_greater_than_list_length(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(larg_nnum([], 1), [])

    def test_edge_case_n_zero(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3, 4, 5], -1)
