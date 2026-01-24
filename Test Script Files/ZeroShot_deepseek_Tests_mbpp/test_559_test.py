import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

    def test_single_number(self):
        self.assertEqual(max_sub_array_sum([5], 1), 5)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)
