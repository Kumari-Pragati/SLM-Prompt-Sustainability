import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_max_sum_of_three_consecutive(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 12)
        self.assertEqual(max_sum_of_three_consecutive([1, 20, 30, 40, 10], 5), 100)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 66)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_sum_of_three_consecutive([10, 20, 30, 40, 50], 5), 150)
