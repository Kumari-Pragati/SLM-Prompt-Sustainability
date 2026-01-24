import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_k_smallest_pairs_empty_lists(self):
        self.assertListEqual(k_smallest_pairs([], [], 0), [])

    def test_k_smallest_pairs_single_element(self):
        self.assertListEqual(k_smallest_pairs([1], [], 1), [(1,)])
        self.assertListEqual(k_smallest_pairs([], [2], 1), [(2,)])

    def test_k_smallest_pairs_simple(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 8, 9], 3), [(1, 2), (7, 2), (3, 8)])

    def test_k_smallest_pairs_large(self):
        self.assertListEqual(k_smallest_pairs([1, 5, 9, 13, 17], [2, 6, 10, 14, 18], 5), [(1, 2), (5, 6), (9, 6), (13, 10), (17, 14)])

    def test_k_smallest_pairs_k_larger_than_len(self):
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 7), [(1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (1, 6)])
