import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(split_two_parts([], 0), ([], []))

    def test_single_element_list(self):
        self.assertEqual(split_two_parts([1], 0), ([1], []))

    def test_list_with_multiple_elements(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))

    def test_list_with_multiple_elements_and_larger_than_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 10), ([1, 2, 3, 4, 5], []))

    def test_list_with_multiple_elements_and_smaller_than_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -1), ([1, 2, 3, 4, 5], []))

    def test_list_with_multiple_elements_and_larger_than_list_with_negative_index(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -3), ([1, 2, 3], [4, 5]))

    def test_list_with_multiple_elements_and_smaller_than_list_with_negative_index(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -6), ([1, 2, 3, 4, 5], []))
