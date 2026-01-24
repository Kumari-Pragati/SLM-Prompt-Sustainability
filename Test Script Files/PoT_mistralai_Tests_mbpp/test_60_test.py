import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 5), 3)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(max_len_sub([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_len_sub([], 0), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_len_sub([-1, -2, -3], 3), 1)

    def test_edge_case_equal_numbers(self):
        self.assertEqual(max_len_sub([1, 1, 1], 3), 1)

    def test_corner_case_adjacent_numbers(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 5), 3)

    def test_corner_case_non_adjacent_numbers(self):
        self.assertEqual(max_len_sub([1, 2, 3, 5, 4], 5), 3)
