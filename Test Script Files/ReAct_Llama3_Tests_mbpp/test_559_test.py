import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_positive_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 15)

    def test_negative_array(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_mixed_array(self):
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5], 5), 5)

    def test_single_element_array(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_zero_array(self):
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 0)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            max_sub_array_sum([], 0)

    def test_array_with_zero_size(self):
        with self.assertRaises(IndexError):
            max_sub_array_sum([1, 2, 3], 0)
