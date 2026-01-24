import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_divisible_by_m_and_n(self):
        nums = [10, 20, 30, 40, 50]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [10, 20, 30, 40, 50])

    def test_divisible_by_m_only(self):
        nums = [5, 10, 15, 20, 25]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [5, 10, 15, 20, 25])

    def test_divisible_by_n_only(self):
        nums = [10, 20, 30, 40, 50]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [10, 20, 30, 40, 50])

    def test_divisible_by_both(self):
        nums = [15, 30, 45, 60, 75]
        m = 3
        n = 5
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [15, 30, 45, 60, 75])

    def test_empty_list(self):
        nums = []
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        nums = [10]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [10])
