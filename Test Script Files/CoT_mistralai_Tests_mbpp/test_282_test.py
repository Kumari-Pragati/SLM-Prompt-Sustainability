import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_sub_list_positive(self):
        self.assertListEqual(sub_list([1, 2, 3], [0, 1, 2]), [1, 0, 0])
        self.assertListEqual(sub_list([-1, -2, -3], [-1, 0, 1]), [-2, -1, -4])
        self.assertListEqual(sub_list([4, 5, 6], [1, 2, 3]), [3, 3, 3])

    def test_sub_list_empty_lists(self):
        self.assertListEqual(sub_list([], []), [])
        self.assertListEqual(sub_list([1], []), [1])
        self.assertListEqual(sub_list([], [1]), [])

    def test_sub_list_different_lengths(self):
        self.assertRaises(ValueError, sub_list, [1, 2, 3], [1, 2])
        self.assertRaises(ValueError, sub_list, [1, 2], [1, 2, 3])

    def test_sub_list_non_list_inputs(self):
        self.assertRaises(TypeError, sub_list, "1", "2")
        self.assertRaises(TypeError, sub_list, [1], "2")
        self.assertRaises(TypeError, sub_list, "1", [2])
