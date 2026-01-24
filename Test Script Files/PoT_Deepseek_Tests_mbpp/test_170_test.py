import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_edge_case_m_equals_n(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 2), 2)

    def test_boundary_case_m_greater_than_n(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 2), 0)

    def test_boundary_case_m_less_than_0(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -1, 3), 10)

    def test_boundary_case_n_greater_than_len_of_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 6), 15)

    def test_corner_case_empty_list(self):
        self.assertEqual(sum_range_list([], 1, 3), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 1, 3), -6)

    def test_corner_case_large_numbers(self):
        self.assertEqual(sum_range_list([1000, 2000, 3000, 4000, 5000], 1, 3), 6000)
