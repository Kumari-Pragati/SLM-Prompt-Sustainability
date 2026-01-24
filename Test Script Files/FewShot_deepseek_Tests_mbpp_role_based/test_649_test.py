import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 2
        n = 8
        self.assertEqual(sum_Range_list(nums, m, n), 33)

    def test_edge_condition(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 0
        n = 0
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_boundary_condition(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 0
        n = 9
        self.assertEqual(sum_Range_list(nums, m, n), 45)

    def test_invalid_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 11
        n = 12
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)
