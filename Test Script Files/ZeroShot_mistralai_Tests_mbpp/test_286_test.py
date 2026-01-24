import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum_repeated([], 3, 2), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([1], 2, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([1], 3, 1), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 2), 15)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 4, 2), 12)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 3, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 2, 2), 7)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 1, 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 2), -15)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 4, 2), -12)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 3, 2), -9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 2, 2), -7)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 1, 2), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 5, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 4, 2), 7)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 3, 2), 5)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 2, 2), 3)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 1, 2), 1)
