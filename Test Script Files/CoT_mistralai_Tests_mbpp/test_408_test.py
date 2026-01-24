import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_empty_k(self):
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 0), [])

    def test_single_pair(self):
        self.assertListEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])
        self.assertListEqual(k_smallest_pairs([1, 2], [3], 1), [[1, 3], [2, 3]])

    def test_multiple_pairs(self):
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 2), [[1, 3], [2, 4]])
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 3), [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]])

    def test_edge_cases(self):
        self.assertListEqual(k_smallest_pairs([], [], 1), [])
        self.assertListEqual(k_smallest_pairs([1], [], 1), [])
        self.assertListEqual(k_smallest_pairs([1], [2], 0), [])
        self.assertListEqual(k_smallest_pairs([1], [2], 2), [[1, 2]])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, k_smallest_pairs, [1], [2], '3')
        self.assertRaises(TypeError, k_smallest_pairs, [1, 2], [3, 4], -1)
