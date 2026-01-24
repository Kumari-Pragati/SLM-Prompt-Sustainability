import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(sub_list([1, 2, 3], [2, 1, 0]), [3, 1, -3])

    def test_subtract_negative_numbers(self):
        self.assertEqual(sub_list([-1, -2, -3], [-2, -1, 0]), [1, 1, -3])

    def test_subtract_empty_lists(self):
        self.assertEqual(sub_list([], []), [])

    def test_subtract_lists_with_different_lengths(self):
        self.assertEqual(sub_list([1, 2, 3], [1, 2]), [0, 1])
