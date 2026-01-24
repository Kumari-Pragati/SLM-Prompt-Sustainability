import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_positive_index_and_length(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 3), ([1, 2, 3], [4, 5]))

    def test_zero_index_and_length(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))

    def test_negative_index_and_length(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], -1), ([], [1, 2, 3, 4]))

    def test_index_greater_than_list_length(self):
        self.assertEqual(split_two_parts([1, 2, 3], 4), ([1, 2, 3], []))

    def test_zero_length_list(self):
        self.assertEqual(split_two_parts([], 0), ([], []))

    def test_empty_list_and_negative_length(self):
        self.assertEqual(split_two_parts([], -1), ([], []))
