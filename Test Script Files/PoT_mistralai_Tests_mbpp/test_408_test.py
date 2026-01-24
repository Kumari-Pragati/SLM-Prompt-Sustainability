import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6], 3), [[1, 2], [1, 4], [7, 2]])

    def test_edge_case_k_0(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6], 0), [])

    def test_edge_case_k_len(self):
        self.assertListEqual(k_smallest_pairs([1, 7, 3], [2, 4, 6], len([1, 7, 3])), [[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [7, 6]])

    def test_edge_case_empty_lists(self):
        self.assertListEqual(k_smallest_pairs([], [], 2), [])

    def test_edge_case_one_list(self):
        self.assertListEqual(k_smallest_pairs([1], [], 1), [[1, None]])
        self.assertListEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])
