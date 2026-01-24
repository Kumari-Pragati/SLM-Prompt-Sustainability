import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 2)

    def test_edge_case_k_zero(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 0), 0)

    def test_edge_case_k_large(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 100), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_corner_case_k_negative(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -1), 0)

    def test_corner_case_k_positive(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 2)
