import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 3
        n = 8
        self.assertEqual(sum_Range_list(nums, m, n), 3+4+5+6+7+8)

    def test_edge_case_m_equals_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 3
        n = 3
        self.assertEqual(sum_Range_list(nums, m, n), nums[m])

    def test_edge_case_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 5
        n = 3
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)

    def test_edge_case_empty_list(self):
        nums = []
        m = 0
        n = 0
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_invalid_input_negative_index(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = -1
        n = 3
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)

    def test_invalid_input_out_of_range_index(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 11
        n = 15
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)
