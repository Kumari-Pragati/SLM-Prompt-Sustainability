import unittest
from mbpp_10_code import small_nnum

class TestSmallNNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 3), [1, 2, 3])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 0), [])

    def test_edge_case_n_equals_one(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 1), [1])

    def test_edge_case_n_equals_length_of_list(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 5), [1, 2, 3, 4, 5])

    def test_edge_case_n_greater_than_length_of_list(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 10), [1, 2, 3, 4, 5])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(small_nnum([-3, -1, -2, -5, -4], 3), [-5, -4, -3])

    def test_corner_case_duplicate_numbers(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4, 1], 3), [1, 1, 2])

    def test_corner_case_empty_list(self):
        self.assertEqual(small_nnum([], 3), [])
