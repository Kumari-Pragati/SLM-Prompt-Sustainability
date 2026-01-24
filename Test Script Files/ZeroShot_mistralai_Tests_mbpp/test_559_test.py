import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, 4], 3), 4)

    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 1), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 2), 5)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4], 4), 5)
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4], 2), 4)
