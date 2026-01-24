import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_sum_range_list_typical(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_sum_range_list_edge_case_start(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_sum_range_list_edge_case_end(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)

    def test_sum_range_list_edge_case_middle(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 9)

    def test_sum_range_list_edge_case_start_end(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_sum_range_list_edge_case_start_end_middle(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_sum_range_list_edge_case_invalid_start(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 6, 6)

    def test_sum_range_list_edge_case_invalid_end(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 1, 6)

    def test_sum_range_list_edge_case_invalid_start_end(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 6, 6)
