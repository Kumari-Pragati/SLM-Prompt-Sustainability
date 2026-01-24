import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_edge_case_start(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_edge_case_end(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 5), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_range_list([1], 0, 0), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
        sum_range_list([], 0, 0)

    def test_edge_case_invalid_start(self):
        with self.assertRaises(IndexError):
        sum_range_list([1, 2, 3, 4, 5], 5, 5)

    def test_edge_case_invalid_end(self):
        with self.assertRaises(IndexError):
        sum_range_list([1, 2, 3, 4, 5], 0, 0)

    def test_edge_case_invalid_range(self):
        with self.assertRaises(IndexError):
        sum_range_list([1, 2, 3, 4, 5], 2, 1)
