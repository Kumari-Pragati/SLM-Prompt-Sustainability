import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 2), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)

    def test_all_positive(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 3), 10)

    def test_all_negative(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 3), -1)

    def test_boundary_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)

    def test_zero_array(self):
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0], 4, 2), 0)

    def test_k_greater_than_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 5), 10)

    def test_k_equal_to_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 4), 10)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 2), 0)
