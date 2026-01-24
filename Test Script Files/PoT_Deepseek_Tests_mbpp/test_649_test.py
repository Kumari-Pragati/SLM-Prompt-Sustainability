import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 3
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_edge_case_m_equals_n(self):
        nums = [1, 2, 3, 4, 5]
        m = 2
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), nums[2])

    def test_boundary_case_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5]
        m = 3
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_boundary_case_m_less_than_zero(self):
        nums = [1, 2, 3, 4, 5]
        m = -1
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_boundary_case_n_greater_than_length_of_nums(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 10
        self.assertEqual(sum_Range_list(nums, m, n), sum(nums))

    def test_invalid_input_m_less_than_zero(self):
        nums = [1, 2, 3, 4, 5]
        m = -1
        n = 2
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)

    def test_invalid_input_n_greater_than_length_of_nums(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 10
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)
