import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_equals_one(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 1), [5])

    def test_edge_case_n_equals_length_of_list(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case_n_greater_than_length_of_list(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])

    def test_corner_case_duplicate_numbers(self):
        self.assertEqual(larg_nnum([5, 5, 4, 4, 3, 3, 2, 2, 1, 1], 3), [5, 4, 3])

    def test_corner_case_empty_list(self):
        self.assertEqual(larg_nnum([], 3), [])
