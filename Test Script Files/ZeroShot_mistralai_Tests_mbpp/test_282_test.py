import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_sub_list_empty_lists(self):
        self.assertListEqual(sub_list([], []), [])

    def test_sub_list_single_element_lists(self):
        self.assertListEqual(sub_list([1], []), [1])
        self.assertListEqual(sub_list([], [1]), [-1])

    def test_sub_list_equal_lists(self):
        self.assertListEqual(sub_list([1, 2, 3], [1, 2, 3]), [0, 0, 0])

    def test_sub_list_different_lengths(self):
        self.assertRaises(ValueError, sub_list, [1, 2, 3], [1, 2])

    def test_sub_list_negative_numbers(self):
        self.assertListEqual(sub_list([-1, 2, -3], [4, -2, 5]), [5, 4, -8])
