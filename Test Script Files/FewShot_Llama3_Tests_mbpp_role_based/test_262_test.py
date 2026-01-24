import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_split_empty_list(self):
        self.assertEqual(split_two_parts([], 0), ([], []))

    def test_split_single_element(self):
        self.assertEqual(split_two_parts([1], 0), ([1], []))

    def test_split_multiple_elements(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))

    def test_split_index_out_of_range(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 10), ([1, 2, 3, 4, 5], []))

    def test_split_negative_index(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -1), ([1, 2, 3, 4, 5], []))
