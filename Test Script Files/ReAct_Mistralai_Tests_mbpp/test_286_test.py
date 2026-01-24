import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), 0)

    def test_single_element_array(self):
        for k in range(1, 6):
            self.assertEqual(max_sub_array_sum_repeated([1], 1, k), 1)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        for k in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum_repeated(arr, len(arr), k), sum(arr))

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        for k in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum_repeated(arr, len(arr), k), max(arr) * k)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        for k in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum_repeated(arr, len(arr), k), max(arr) * k)

    def test_zero_in_array(self):
        arr = [0, 1, -2, 3, -4, 5]
        for k in range(1, len(arr) + 1):
            self.assertEqual(max_sub_array_sum_repeated(arr, len(arr), k), max(arr) * k)

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated([1], 1, 0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated([1], 0, 1)

    def test_invalid_type_a(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum_repeated('str', 1, 1)

    def test_invalid_type_n(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum_repeated([1], 'str', 1)

    def test_invalid_type_k(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum_repeated([1], 1, 'str')
