import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        nums = [10, 20, 30, 40]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [10, 20, 30, 40])

    def test_edge_case_with_zero(self):
        nums = [0, 20, 30, 40]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [0, 20, 30, 40])

    def test_edge_case_with_single_number(self):
        nums = [15]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [15])

    def test_edge_case_with_no_divisible_numbers(self):
        nums = [17, 19, 23]
        m = 5
        n = 10
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [])

    def test_typical_case_with_large_numbers(self):
        nums = list(range(1, 10001))
        m = 100
        n = 200
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, list(range(100, 10001, 100)))
