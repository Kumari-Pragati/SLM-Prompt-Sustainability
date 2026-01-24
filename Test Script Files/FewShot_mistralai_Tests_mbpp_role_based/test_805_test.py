import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sum_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(max_sum_list([[1]]), [[1]])

    def test_multiple_lists_with_same_sum(self):
        self.assertEqual(max_sum_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_multiple_lists_with_different_sums(self):
        self.assertEqual(max_sum_list([[1, 2], [3, 4], [5, 6, 7]]), [[5, 6, 7]])

    def test_negative_numbers(self):
        self.assertEqual(max_sum_list([[-1, -2], [-3, -4]]), [[-1, -2]])

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(max_sum_list([[1, -2], [3, 4]]), [[3, 4]])
