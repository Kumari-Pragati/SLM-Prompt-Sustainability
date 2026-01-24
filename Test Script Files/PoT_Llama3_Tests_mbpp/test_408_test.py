import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(k_smallest_pairs([1, 4, 3], [2, 5, 6], 3), [[1, 2], [1, 5], [1, 6]])

    def test_edge_case_k_zero(self):
        self.assertEqual(k_smallest_pairs([1, 4, 3], [2, 5, 6], 0), [])

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(k_smallest_pairs([1, 4, 3], [2, 5, 6], 6), [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(k_smallest_pairs([1, 4, 3], [2, 5, 6], 10), [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            k_smallest_pairs('a', [1, 2, 3], 2)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            k_smallest_pairs([1, 2, 3], [1, 2], 3)
