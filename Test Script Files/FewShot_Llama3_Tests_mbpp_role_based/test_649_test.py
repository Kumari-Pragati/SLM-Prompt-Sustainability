import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_sum_range_list_positive_numbers(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 10)

    def test_sum_range_list_zero(self):
        nums = [1, 2, 3, 4, 5]
        m = 0
        n = 0
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_sum_range_list_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        m = 2
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), -6)

    def test_sum_range_list_out_of_range(self):
        nums = [1, 2, 3, 4, 5]
        m = 5
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 5)

    def test_sum_range_list_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        m = 5
        n = 'a'
        with self.assertRaises(TypeError):
            sum_Range_list(nums, m, n)
