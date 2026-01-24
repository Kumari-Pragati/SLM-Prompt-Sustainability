import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6], 3), [[1, 2], [1, 4], [7, 2]])
        self.assertListEqual(k_smallest_pairs([4], [5, 6], 1), [[4, 5]])
        self.assertListEqual(k_smallest_pairs([1, 3, 5], [], 2), [[1, 0], [3, 0]])
        self.assertListEqual(k_smallest_pairs([], [2, 4], 1), [])

    def test_edge_cases(self):
        self.assertListEqual(k_smallest_pairs([1], [2], 1), [[1, 0]])
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 0), [])
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 2), [[1, 0], [2, 1], [1, 2]])
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 3), [[1, 0], [2, 1], [1, 2], [3, 0]])
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 4), [[1, 0], [2, 1], [1, 2], [3, 0], [1, 3]])

    def test_complex(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6, 8], 3), [[1, 2], [1, 4], [7, 2]])
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6, 8, 9], 4), [[1, 2], [1, 4], [7, 2], [3, 3]])
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6, 8, 9, 10], 5), [[1, 2], [1, 4], [7, 2], [3, 3], [1, 5]])
