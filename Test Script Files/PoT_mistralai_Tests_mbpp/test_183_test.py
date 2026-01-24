import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 4)
        self.assertEqual(count_pairs([10, 15, 3, 7], 4, 7), 1)
        self.assertEqual(count_pairs([-2, -1, 1, 2], 4, 1), 2)

    def test_edge_case_empty(self):
        self.assertEqual(count_pairs([], 0, 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_pairs([1], 1, 0), 0)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(count_pairs([1, 2], 2, 3), 0)

    def test_edge_case_k_less_than_0(self):
        self.assertEqual(count_pairs([1, 2], 2, -1), 0)

    def test_corner_case_same_elements(self):
        self.assertEqual(count_pairs([1, 1], 2, 0), 1)
