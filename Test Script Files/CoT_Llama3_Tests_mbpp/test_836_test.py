import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_max_sub_array_sum_positive(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)

    def test_max_sub_array_sum_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_max_sub_array_sum_zero(self):
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 1)

    def test_max_sub_array_sum_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_max_sub_array_sum_empty_array(self):
        with self.assertRaises(IndexError):
            max_sub_array_sum([], 0)

    def test_max_sub_array_sum_array_with_one_element(self):
        with self.assertRaises(IndexError):
            max_sub_array_sum([1], 0)
