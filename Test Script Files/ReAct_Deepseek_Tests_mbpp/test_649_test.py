import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = 2
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 15)

    def test_edge_case_m_equals_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = 2
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), nums[m])

    def test_edge_case_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = 5
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_edge_case_empty_list(self):
        nums = []
        m = 0
        n = 0
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_edge_case_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        m = 1
        n = 3
        self.assertEqual(sum_Range_list(nums, m, n), -7)

    def test_edge_case_large_numbers(self):
        nums = [1000000000, 2000000000, 3000000000]
        m = 0
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), 6000000000)
