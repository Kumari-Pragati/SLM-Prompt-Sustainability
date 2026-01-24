import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 3), 12)
        self.assertEqual(max_sub_array_sum([1, -2, 3, 4, -5], 4), 6)
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 3), -3)
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, -5], 5), 6)

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 1), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), -1)

    def test_zero_size(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], 0), 0)

    def test_negative_size(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], -1), 0)
        self.assertEqual(max_sub_array_sum([1, 2, 3], -3), 0)
