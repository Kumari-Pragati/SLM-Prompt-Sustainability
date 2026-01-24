import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], filter_oddnumbers([]))

    def test_single_number(self):
        for num in [1, 3, 5, 7, 9]:
            self.assertListEqual([num], filter_oddnumbers([num]))

    def test_positive_numbers(self):
        for nums in [
            [1, 2, 3, 4, 5],
            [10, 11, 12, 13, 14, 15],
            [100, 101, 102, 103, 104, 105, 106],
        ]:
            self.assertListEqual([num for num in nums if num % 2 != 0], filter_oddnumbers(nums))

    def test_negative_numbers(self):
        for nums in [
            [-1, -2, -3, -4, -5],
            [-10, -11, -12, -13, -14, -15],
            [-100, -101, -102, -103, -104, -105, -106],
        ]:
            self.assertListEqual([num for num in nums if num % 2 != 0], filter_oddnumbers(nums))

    def test_mixed_numbers(self):
        for nums in [
            [1, -2, 3, -4, 5, -6],
            [10, -11, 12, -13, 14, -15, 16, -17],
            [100, -101, 102, -103, 104, -105, 106, -107, 108, -109],
        ]:
            self.assertListEqual([num for num in nums if num % 2 != 0], filter_oddnumbers(nums))

    def test_zero(self):
        self.assertListEqual([], filter_oddnumbers([0]))
