import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertListEqual(small_nnum([10, 20, 30, 40, 50], 3), [10, 20, 30])

    def test_edge_case_empty_list(self):
        self.assertListEqual(small_nnum([], 1), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(small_nnum([1], 1), [1])

    def test_edge_case_single_element_n_greater_than_list_length(self):
        self.assertListEqual(small_nnum([1], 2), [1, 1])

    def test_edge_case_single_element_negative_n(self):
        self.assertRaises(ValueError, small_nnum, [1], -1)

    def test_edge_case_negative_numbers(self):
        self.assertListEqual(small_nnum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])

    def test_corner_case_duplicates(self):
        self.assertListEqual(small_nnum([1, 1, 2, 3, 4], 3), [1, 1, 2])
