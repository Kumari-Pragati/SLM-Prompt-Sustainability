import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_edge_case_m_equals_n(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 2), 2)

    def test_boundary_case_m_less_than_0(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -1, 2), 7)

    def test_boundary_case_n_greater_than_len_of_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 6), 15)

    def test_special_case_empty_list(self):
        self.assertEqual(sum_range_list([], 0, 0), 0)

    def test_invalid_input_m_greater_than_n(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 3, 2)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], -1, 2)

    def test_invalid_input_out_of_range_index(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 5, 6)
