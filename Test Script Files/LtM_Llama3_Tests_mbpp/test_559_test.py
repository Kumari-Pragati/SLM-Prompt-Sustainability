import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sub_array_sum([-1], 1), -1)

    def test_positive_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 15)

    def test_negative_array(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_mixed_array(self):
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5], 5), 5)

    def test_array_with_zero(self):
        self.assertEqual(max_sub_array_sum([0, 1, 2, 3, 4], 5), 4)

    def test_array_with_negative_and_zero(self):
        self.assertEqual(max_sub_array_sum([-1, 0, 1, -2, 3], 5), 3)

    def test_array_with_all_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_array_with_all_positive(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 15)

    def test_array_with_max_value(self):
        self.assertEqual(max_sub_array_sum([10, 20, 30, 40, 50], 5), 50)

    def test_array_with_min_value(self):
        self.assertEqual(max_sub_array_sum([-10, -20, -30, -40, -50], 5), -10)
