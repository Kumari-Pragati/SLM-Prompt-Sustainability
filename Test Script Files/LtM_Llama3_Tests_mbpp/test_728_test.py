import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(sum_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(sum_list([1], [2]), [3])
        self.assertEqual(sum_list([1, 2], [3, 4]), [4, 6])

    def test_lists_of_different_lengths(self):
        self.assertEqual(sum_list([1, 2, 3], [4]), [5, 6, 3])
        self.assertEqual(sum_list([1, 2], [3, 4, 5]), [4, 6])

    def test_lists_with_negative_numbers(self):
        self.assertEqual(sum_list([-1, 2], [3, -4]), [1, -2])
        self.assertEqual(sum_list([1, -2], [3, 4]), [4, 2])

    def test_lists_with_zero(self):
        self.assertEqual(sum_list([0, 1], [2, 3]), [2, 3])
        self.assertEqual(sum_list([1, 2], [0, 3]), [1, 3])
