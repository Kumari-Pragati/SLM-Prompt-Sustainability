import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_empty_k(self):
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 0), [])

    def test_one_element_k(self):
        self.assertListEqual(k_smallest_pairs([1], [2, 3, 4], 1), [[1, 2]])
        self.assertListEqual(k_smallest_pairs([1, 2], [3, 4], 1), [[1, 3], [2, 4]])

    def test_k_larger_than_length(self):
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 4), [
            [1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]
        ])

    def test_k_equal_to_length(self):
        self.assertListEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 3), [
            [1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4]
        ])

    def test_one_list_empty(self):
        self.assertListEqual(k_smallest_pairs([], [1, 2, 3], 1), [])
        self.assertListEqual(k_smallest_pairs([1, 2], [], 1), [])

    def test_one_list_single_element(self):
        self.assertListEqual(k_smallest_pairs([1], [], 1), [])
        self.assertListEqual(k_smallest_pairs([], [1], 1), [])

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            k_smallest_pairs([1, 2, 3], [4, 5, 6], -1)
