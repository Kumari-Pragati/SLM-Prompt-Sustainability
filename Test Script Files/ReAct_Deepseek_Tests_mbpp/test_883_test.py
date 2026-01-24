import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        nums = [10, 20, 30, 40]
        m = 5
        n = 10
        expected_result = [10, 20, 30, 40]
        self.assertEqual(div_of_nums(nums, m, n), expected_result)

    def test_edge_case_no_divisible_numbers(self):
        nums = [11, 13, 17, 19]
        m = 2
        n = 3
        expected_result = []
        self.assertEqual(div_of_nums(nums, m, n), expected_result)

    def test_edge_case_all_numbers_divisible(self):
        nums = [10, 20, 30, 40]
        m = 2
        n = 5
        expected_result = nums
        self.assertEqual(div_of_nums(nums, m, n), expected_result)

    def test_edge_case_m_equals_n(self):
        nums = [10, 20, 30, 40]
        m = 2
        n = 2
        expected_result = nums
        self.assertEqual(div_of_nums(nums, m, n), expected_result)

    def test_edge_case_m_and_n_are_zero(self):
        nums = [10, 20, 30, 40]
        m = 0
        n = 0
        expected_result = []
        self.assertEqual(div_of_nums(nums, m, n), expected_result)

    def test_error_case_m_and_n_are_negative(self):
        nums = [10, 20, 30, 40]
        m = -2
        n = -5
        with self.assertRaises(ValueError):
            div_of_nums(nums, m, n)
