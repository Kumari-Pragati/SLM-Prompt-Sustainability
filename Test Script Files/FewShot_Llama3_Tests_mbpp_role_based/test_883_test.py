import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_div_of_nums_positive_numbers(self):
        nums = [12, 24, 36, 48, 60]
        m = 3
        n = 4
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [12, 24, 36, 48])

    def test_div_of_nums_zero_divisor(self):
        nums = [12, 24, 36, 48, 60]
        m = 0
        n = 4
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [])

    def test_div_of_nums_negative_numbers(self):
        nums = [-12, -24, -36, -48, -60]
        m = 3
        n = 4
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [])

    def test_div_of_nums_empty_list(self):
        nums = []
        m = 3
        n = 4
        result = div_of_nums(nums, m, n)
        self.assertEqual(result, [])

    def test_div_of_nums_invalid_type(self):
        nums = "hello"
        m = 3
        n = 4
        with self.assertRaises(TypeError):
            div_of_nums(nums, m, n)
