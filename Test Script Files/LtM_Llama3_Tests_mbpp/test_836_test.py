import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sub_array_sum([-1], 1), 1)

    def test_positive_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)

    def test_negative_array(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)

    def test_mixed_array(self):
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, -5], 5), 6)

    def test_array_with_max_at_start(self):
        self.assertEqual(max_sub_array_sum([5, -2, -3, 4, -5], 5), 5)

    def test_array_with_max_at_end(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, 4, 5], 5), 5)

    def test_array_with_max_in_middle(self):
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, 5], 5), 9)

    def test_array_with_max_at_start_and_end(self):
        self.assertEqual(max_sub_array_sum([5, 2, 3, 4, 5], 5), 10)

    def test_array_with_max_at_start_and_end_and_middle(self):
        self.assertEqual(max_sub_array_sum([5, 2, 3, 4, 5, 5], 6), 12)
