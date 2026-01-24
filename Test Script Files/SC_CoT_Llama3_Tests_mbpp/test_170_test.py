import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_edge_case_start(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_edge_case_end(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 5), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_range_list([1], 1, 1), 1)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 5, 6)

    def test_edge_case_invalid_input_start(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 5, 1)

    def test_edge_case_invalid_input_end(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 1, 6)

    def test_edge_case_invalid_input_range(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 6, 6)
