import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)

    def test_single_negative_number(self):
        self.assertEqual(max_sub_array_sum([-1], 1), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-2, -1, 0, 1, 2], 5), 3)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_size_greater_than_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], 4), 6)

    def test_size_less_than_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 3), 6)

    def test_size_zero(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 0), 0)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum([1, 2, 3, 4], -1)
