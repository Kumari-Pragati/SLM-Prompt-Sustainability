import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)

    def test_simple_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 5)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_all_zeros(self):
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 0)

    def test_negative_and_positive(self):
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5], 5), 3)

    def test_negative_only(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 5)

    def test_positive_only(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)
