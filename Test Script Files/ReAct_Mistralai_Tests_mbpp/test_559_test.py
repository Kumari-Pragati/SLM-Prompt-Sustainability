import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 1), 0)

    def test_single_element_array(self):
        for num in range(-10, 11):
            self.assertEqual(max_sub_array_sum([num], 1), num)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        for size in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum(arr, size), sum(arr))

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        for size in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum(arr, size), max(arr))

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        for size in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum(arr, size), max(arr))

    def test_zero_sum_array(self):
        arr = [0, 0, 0]
        for size in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum(arr, size), 0)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3], -1)

    def test_empty_size(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3], 0)
