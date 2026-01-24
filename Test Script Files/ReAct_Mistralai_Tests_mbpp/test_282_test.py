import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(sub_list([], []), [])
        self.assertListEqual(sub_list([], [1]), [0])
        self.assertListEqual(sub_list([1], []), [1])

    def test_single_element_lists(self):
        self.assertListEqual(sub_list([1], [1]), [0])
        self.assertListEqual(sub_list([2], [1]), [1])
        self.assertListEqual(sub_list([1], [2]), [-1])

    def test_equal_length_lists(self):
        self.assertListEqual(sub_list([1, 2, 3], [2, 1, 0]), [1, 1, -3])
        self.assertListEqual(sub_list([5, 3, 1], [2, 4, 6]), [-3, -1, -5])

    def test_different_length_lists(self):
        self.assertListEqual(sub_list([1, 2, 3], [2, 1]), [1, 1, -1])
        self.assertListEqual(sub_list([1, 2, 3], [2, 1, 0, 4]), [1, 1, -1, -4])

    def test_negative_numbers(self):
        self.assertListEqual(sub_list([-1, -2, -3], [2, 1]), [3, 3, 5])
        self.assertListEqual(sub_list([-1, -2, -3], [2, 1, 0]), [3, 3, 3, -3])

    def test_zero(self):
        self.assertListEqual(sub_list([0], [1]), [-1])
        self.assertListEqual(sub_list([1], [0]), [1])
        self.assertListEqual(sub_list([0], [0]), [0])
