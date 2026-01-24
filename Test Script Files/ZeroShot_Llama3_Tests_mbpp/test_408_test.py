import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_k_smallest_pairs(self):
        self.assertEqual(k_smallest_pairs([1, 7, 11], [2, 9], 3), [[1, 2], [1, 9], [2, 7]])
        self.assertEqual(k_smallest_pairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 2]])
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 4), [[1, 4], [1, 5], [1, 6], [2, 4]])
        self.assertEqual(k_smallest_pairs([1, 3, 5], [2, 4, 6], 3), [[1, 2], [1, 4], [2, 3]])

    def test_k_smallest_pairs_empty(self):
        self.assertEqual(k_smallest_pairs([], [], 3), [])
        self.assertEqual(k_smallest_pairs([1], [], 3), [])
        self.assertEqual(k_smallest_pairs([], [1], 3), [])

    def test_k_smallest_pairs_k_zero(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 0), [])

    def test_k_smallest_pairs_k_greater_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 10), [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]])
