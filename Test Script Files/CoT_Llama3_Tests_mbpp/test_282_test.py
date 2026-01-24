import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_sub_list_with_positive_numbers(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_sub_list_with_negative_numbers(self):
        self.assertEqual(sub_list([-1, -2, -3], [-4, -5, -6]), [3, 3, 3])

    def test_sub_list_with_mixed_numbers(self):
        self.assertEqual(sub_list([1, -2, 3], [4, -5, 6]), [-3, 7, -3])

    def test_sub_list_with_empty_list(self):
        self.assertEqual(sub_list([], [1, 2, 3]), [])

    def test_sub_list_with_single_element_list(self):
        self.assertEqual(sub_list([1], [2]), [-1])

    def test_sub_list_with_lists_of_different_lengths(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5]), [1, -1, -2])

    def test_sub_list_with_lists_of_zero_length(self):
        self.assertEqual(sub_list([], []), [])
