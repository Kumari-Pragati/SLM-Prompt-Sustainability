import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(split_two_parts([], 2), ([], []))

    def test_single_element_list(self):
        self.assertEqual(split_two_parts([1], 1), ([1], []))
        self.assertEqual(split_two_parts([1], 2), ([1], []))

    def test_list_with_two_elements(self):
        self.assertEqual(split_two_parts([1, 2], 1), ([1], [2]))
        self.assertEqual(split_two_parts([1, 2], 2), ([1, 2], []))

    def test_list_with_more_than_two_elements(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4], 2), ([1, 2], [3, 4]))
        self.assertEqual(split_two_parts([1, 2, 3, 4], 3), ([1, 2, 3], [4]))
