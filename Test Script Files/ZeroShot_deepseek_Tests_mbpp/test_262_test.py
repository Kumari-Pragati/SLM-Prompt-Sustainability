import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_split_two_parts_with_empty_list(self):
        self.assertEqual(split_two_parts([], 0), ([], []))

    def test_split_two_parts_with_small_L(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))

    def test_split_two_parts_with_large_L(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 6), ([1, 2, 3, 4, 5], []))

    def test_split_two_parts_with_negative_L(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -1), ([], [1, 2, 3, 4, 5]))

    def test_split_two_parts_with_float_L(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2.5), ([1], [2, 3, 4, 5]))
