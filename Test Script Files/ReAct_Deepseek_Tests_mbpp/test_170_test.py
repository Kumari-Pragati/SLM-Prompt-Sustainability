import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_edge_case_m_equals_n(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 2), 2)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 2), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_range_list([], 0, 0), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 1, 3), -6)

    def test_edge_case_large_numbers(self):
        self.assertEqual(sum_range_list([1000000, 2000000, 3000000, 4000000, 5000000], 1, 3), 6000000)

    def test_edge_case_out_of_range(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 10, 11)
