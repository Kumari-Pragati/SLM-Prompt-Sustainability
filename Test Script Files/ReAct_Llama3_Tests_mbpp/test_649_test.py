import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_sum_Range_list_typical(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 10)

    def test_sum_Range_list_edge_case_start(self):
        nums = [1, 2, 3, 4, 5]
        m = 0
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_sum_Range_list_edge_case_end(self):
        nums = [1, 2, 3, 4, 5]
        m = 2
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_sum_Range_list_edge_case_single(self):
        nums = [1, 2, 3, 4, 5]
        m = 3
        n = 3
        self.assertEqual(sum_Range_list(nums, m, n), 4)

    def test_sum_Range_list_edge_case_empty(self):
        nums = []
        m = 0
        n = 0
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_sum_Range_list_edge_case_invalid(self):
        nums = [1, 2, 3, 4, 5]
        m = 5
        n = 5
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)
