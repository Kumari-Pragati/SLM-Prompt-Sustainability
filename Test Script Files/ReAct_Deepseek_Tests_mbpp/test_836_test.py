import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)

    def test_all_positive(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)

    def test_all_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([-2, -1, 0, 1, 2], 5), 3)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_large_numbers(self):
        self.assertEqual(max_sub_array_sum([1000, 2000, 3000, 4000], 4), 4)

    def test_large_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1000, -2000, -3000, -4000], 4), 1)

    def test_large_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([-1000, -2000, 3000, 4000], 4), 4)
