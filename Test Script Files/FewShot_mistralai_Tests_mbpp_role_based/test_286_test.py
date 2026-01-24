import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 3, 2), 12)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 2, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 1, 2), 5)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 2), 15)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([0, -1, 2, -3, 4], 3, 2), 6)
        self.assertEqual(max_sub_array_sum_repeated([0, -1, 2, -3, 4], 2, 2), 3)
        self.assertEqual(max_sub_array_sum_repeated([0, -1, 2, -3, 4], 1, 2), 2)
        self.assertEqual(max_sub_array_sum_repeated([0, -1, 2, -3, 4], 5, 2), 6)

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum_repeated([], 3, 2), 0)

    def test_negative_n_and_k(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], -3, 2), 0)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, -2), 0)

    def test_zero_n_or_k(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 0, 2), 0)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 0), 0)
