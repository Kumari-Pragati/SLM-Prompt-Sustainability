import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_alternates([]), (0, 0))

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(sum_of_alternates([num]), ((num, 0)))

    def test_even_length(self):
        for nums in [(1, 2, 3, 4), (5, 6, 7, 8), (9, 0, 1, 2, 3), (4, 3, 2, 1)]:
            self.assertEqual(sum_of_alternates(nums), ((sum(nums[::2]), sum(nums[1::2]))) )

    def test_odd_length(self):
        for nums in [(1, 2, 3, 4, 5), (6, 7, 8, 9, 0), (1, 0, 1, 2, 3, 4)]:
            self.assertEqual(sum_of_alternates(nums), ((sum(nums[::2]), sum(nums[1::2]))))

    def test_negative_numbers(self):
        for nums in [(-1, 0, 1), (-2, -3, -4, -5), (-6, -7, -8, -9)]:
            self.assertEqual(sum_of_alternates(nums), ((sum(nums[::2]), sum(nums[1::2]))) )

    def test_zero(self):
        self.assertEqual(sum_of_alternates([0]), ((0, 0)))
