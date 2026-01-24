import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5, 6], 6), 6)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5, 6, 7], 7), 7)

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), 1)
        self.assertEqual(max_sub_array_sum([0], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5, -6], 6), 1)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5], 5), 3)
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5, -6], 6), 3)

    def test_zero_in_list(self):
        self.assertEqual(max_sub_array_sum([0, 1, -2, 3, 0, 4], 6), 3)
