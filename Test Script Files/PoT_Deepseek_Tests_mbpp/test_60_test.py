import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_len_sub([10, 22, 9, 33, 21, 50, 41, 60, 80], 9), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(max_len_sub([5], 1), 1)

    def test_boundary_case_empty_array(self):
        self.assertEqual(max_len_sub([], 0), 0)

    def test_corner_case_all_elements_differ_by_more_than_one(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 1)

    def test_corner_case_all_elements_differ_by_one(self):
        self.assertEqual(max_len_sub([1, 2, 2, 3, 3], 5), 3)

    def test_corner_case_repeated_elements(self):
        self.assertEqual(max_len_sub([1, 2, 2, 1, 3, 3, 2, 1], 8), 4)
