import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_k_smallest_pairs(self):
        self.assertEqual(k_smallest_pairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])
        self.assertEqual(k_smallest_pairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])
        self.assertEqual(k_smallest_pairs([1, 2], [3], 3), [[1, 3], [2, 3]])
        self.assertEqual(k_smallest_pairs([], [], 0), [])
        self.assertEqual(k_smallest_pairs([1], [2, 3, 4], 3), [[1, 2], [1, 3], [1, 4]])
