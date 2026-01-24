import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6], 2), [[1, 2], [7, 4]])
        self.assertListEqual(k_smallest_pairs([4, 5, 6], [1, 2, 3], 3), [[4, 1], [5, 2], [6, 3]])

    def test_edge_cases(self):
        self.assertListEqual(k_smallest_pairs([], [], 0), [])
        self.assertListEqual(k_smallest_pairs([1], [], 1), [[1, None]])
        self.assertListEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])
        self.assertListEqual(k_smallest_pairs([1], [2], 2), [[1, 2], [1, None]])
        self.assertListEqual(k_smallest_pairs([1], [2], 3), [[1, 2], [1, None]])

    def test_boundary(self):
        self.assertListEqual(k_smallest_pairs([1], [2], 0), [])
        self.assertListEqual(k_smallest_pairs([1], [2], 10), [[1, 2], [1, None], [1, None], [1, None], [1, None], [1, None], [1, None], [1, None], [1, None], [1, None]])

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, k_smallest_pairs, [1], [2], -1)
        self.assertRaises(ValueError, k_smallest_pairs, [1], [2], len([1]) + len([2]) + 1)
