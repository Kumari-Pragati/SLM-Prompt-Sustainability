import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_max_sum_of_three_consecutive(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 9)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), 11)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7], 7), 12)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8], 8), 14)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 15)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 17)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 18)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 20)
