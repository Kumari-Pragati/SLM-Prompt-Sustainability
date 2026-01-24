import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_k_smallest_pairs_empty_input(self):
        self.assertEqual(k_smallest_pairs([], [], 1), [])

    def test_k_smallest_pairs_single_element(self):
        self.assertEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])

    def test_k_smallest_pairs_k_greater_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5], 10), [[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]])

    def test_k_smallest_pairs_k_equal_to_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5], 3), [[1, 4], [1, 5], [2, 4]])

    def test_k_smallest_pairs_k_smaller_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5], 2), [[1, 4], [1, 5]])

    def test_k_smallest_pairs_negative_numbers(self):
        self.assertEqual(k_smallest_pairs([-1, 0, 1], [2, 3, 4], 3), [[-1, 2], [-1, 3], [0, 2]])
