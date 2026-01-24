import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([-1], 1, 1), -1)

    def test_positive_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 1), 15)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 2, 3), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 1), -15)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 2, 3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 5, 1), 8)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 2, 3), 5)

    def test_zero(self):
        self.assertEqual(max_sub_array_sum_repeated([0], 1, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([0, 0], 2, 1), 0)

    def test_negative_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], -1, 1), TraceError)

    def test_negative_k(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 1, -1), TraceError)
