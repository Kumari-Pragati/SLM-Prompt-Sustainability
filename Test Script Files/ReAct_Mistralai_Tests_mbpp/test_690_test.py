import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], mul_consecutive_nums([]))

    def test_single_element_list(self):
        self.assertListEqual([], mul_consecutive_nums([1]))

    def test_two_elements_list(self):
        self.assertListEqual([1], mul_consecutive_nums([1, 2]))

    def test_positive_numbers_list(self):
        self.assertListEqual([2, 3, 4, 5], mul_consecutive_nums([1, 2, 3, 4, 5]))

    def test_negative_numbers_list(self):
        self.assertListEqual([-2, -3, -4, -5], mul_consecutive_nums([-1, -2, -3, -4, -5]))

    def test_mixed_numbers_list(self):
        self.assertListEqual([-2, 3, 4, -5], mul_consecutive_nums([-1, 2, 3, -4, 5]))

    def test_zero_in_list(self):
        self.assertListEqual([0], mul_consecutive_nums([0, 1, 2, 3, 4]))
        self.assertListEqual([], mul_consecutive_nums([0, 0, 1, 2, 3, 4]))

    def test_duplicate_numbers_list(self):
        self.assertListEqual([2, 4, 4, 8], mul_consecutive_nums([2, 2, 2, 4, 4]))
