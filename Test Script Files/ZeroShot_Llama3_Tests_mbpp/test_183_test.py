import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_count_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 2)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 4), 1)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 5), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 6), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 0), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -1), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -2), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -3), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -4), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, -5), 0)

    def test_count_pairs_edge_cases(self):
        self.assertEqual(count_pairs([], 0, 0), 0)
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1], 1, 1), 0)
        self.assertEqual(count_pairs([1, 2], 2, 0), 0)
        self.assertEqual(count_pairs([1, 2], 2, 1), 0)
