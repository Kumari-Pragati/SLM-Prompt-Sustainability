import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 2), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)

    def test_all_positive(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 2), 10)

    def test_all_negative(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)

    def test_zero(self):
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0], 4, 2), 0)

    def test_large_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([100, 200, 300, 400], 4, 2), 1000)

    def test_k_equals_1(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 1), 10)

    def test_k_equals_0(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 0), -2147483648)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 2), -2147483648)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum_repeated("not an array", 0, 2)
