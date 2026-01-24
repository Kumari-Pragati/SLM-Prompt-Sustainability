import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_split_two_parts(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4], [5]))
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 6), ([1, 2, 3, 4, 5], []))

    def test_split_two_parts_edge_cases(self):
        self.assertEqual(split_two_parts([], 0), ([], []))
        self.assertEqual(split_two_parts([1], 0), ([], [1]))
        self.assertEqual(split_two_parts([1], 1), ([1], []))
