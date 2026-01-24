import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(split_two_parts([], 2), ([], []))

    def test_single_element_list(self):
        self.assertEqual(split_two_parts([1], 1), ([1], []))
        self.assertEqual(split_two_parts([1], 2), ([1], []))

    def test_multiple_elements_list(self):
        self.assertEqual(split_two_parts([1, 2, 3], 1), ([1], [2, 3]))
        self.assertEqual(split_two_parts([1, 2, 3], 2), ([1, 2], [3]))
        self.assertEqual(split_two_parts([1, 2, 3], 3), ([1, 2], [3]))

    def test_negative_index(self):
        self.assertEqual(split_two_parts([1, 2, 3], -1), ([], [1, 2, 3]))
        self.assertEqual(split_two_parts([1, 2, 3], -2), ([], [1, 2])

    def test_zero_index(self):
        self.assertEqual(split_two_parts([1, 2, 3], 0), ([], [1, 2, 3]))

    def test_larger_index(self):
        self.assertEqual(split_two_parts([1, 2, 3], 4), ([1, 2, 3], []))
