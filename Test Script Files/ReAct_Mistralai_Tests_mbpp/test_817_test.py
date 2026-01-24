import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 2, 3), [])

    def test_single_number(self):
        for m, n in [(2, 2), (3, 3), (2, 3), (3, 2)]:
            self.assertListEqual(div_of_nums([m], m, n), [m])
            self.assertListEqual(div_of_nums([n], m, n), [n])

    def test_multiple_numbers(self):
        test_data = [
            ([1, 2, 3, 4, 5], 2, 3, [2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 3, 2, [1, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 4, 5, [1, 2, 3]),
            ([1, 2, 3, 4, 5], 5, 4, [1, 2, 3, 5]),
            ([1, 2, 3, 4, 5], 6, 7, []),
            ([1, 2, 3, 4, 5], 7, 6, []),
        ]
        for nums, m, n, expected in test_data:
            self.assertListEqual(div_of_nums(nums, m, n), expected)

    def test_negative_numbers(self):
        test_data = [
            ([-1, -2, -3, -4, -5], 2, 3, [-2, -3, -4, -5]),
            ([-1, -2, -3, -4, -5], 3, 2, [-1, -3, -4, -5]),
            ([-1, -2, -3, -4, -5], 4, 5, [-1, -2, -3]),
            ([-1, -2, -3, -4, -5], 5, 4, [-1, -2, -3, -5]),
            ([-1, -2, -3, -4, -5], 6, 7, []),
            ([-1, -2, -3, -4, -5], 7, 6, []),
        ]
        for nums, m, n, expected in test_data:
            self.assertListEqual(div_of_nums(nums, m, n), expected)

    def test_zero(self):
        self.assertListEqual(div_of_nums([0], 2, 3), [])
        self.assertListEqual(div_of_nums([0], 3, 2), [])
