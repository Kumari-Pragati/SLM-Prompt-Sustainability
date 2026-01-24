import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 4)
        self.assertEqual(count_pairs([10, 20, 30, 40, 50], 5, 10), 4)

    def test_edge_case_same_elements(self):
        self.assertEqual(count_pairs([1, 1, 2, 3, 4], 5, 0), 1)
        self.assertEqual(count_pairs([1, 1, 1, 2, 3], 5, 0), 2)

    def test_edge_case_no_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 6), 0)
        self.assertEqual(count_pairs([10, 20, 30, 40, 50], 5, 60), 0)

    def test_negative_k(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -1), 0)
        self.assertEqual(count_pairs([10, 20, 30, 40, 50], 5, -10), 0)

    def test_invalid_n(self):
        self.assertRaises(ValueError, count_pairs, [], 5, 1)
        self.assertRaises(ValueError, count_pairs, [1], -1, 1)
