import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(k_smallest_pairs([], [], 1), [])

    def test_single_element_inputs(self):
        self.assertEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])

    def test_k_greater_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5], 10), [[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]])

    def test_k_equal_to_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 3), [[1, 4], [1, 5], [2, 4]])

    def test_k_smaller_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 2), [[1, 6], [2, 6]])

    def test_k_smaller_than_length_with_duplicates(self):
        self.assertEqual(k_smallest_pairs([1, 2, 2, 3, 3, 3], [4, 5, 5, 6, 7, 8], 2), [[1, 4], [2, 4]])

    def test_k_smaller_than_length_with_duplicates_and_zero(self):
        self.assertEqual(k_smallest_pairs([0, 0, 1, 2, 2, 3], [4, 5, 5, 6, 7, 8], 2), [[0, 4], [0, 5]])
