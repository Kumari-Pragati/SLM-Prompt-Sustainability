import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 1), 2)
        self.assertEqual(count_pairs([10, 5, 2, 4], 4, 3), 1)
        self.assertEqual(count_pairs([-1, -2, -3, -4], 4, 1), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(count_pairs([], 0, 0), 0)
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1, 2], 2, 0), 0)
        self.assertEqual(count_pairs([1, 2], 2, 3), 0)
        self.assertEqual(count_pairs([1, 2], 2, 1), 1)
        self.assertEqual(count_pairs([1, 2, 2, 2], 4, 0), 0)
        self.assertEqual(count_pairs([1, 2, 2, 2], 4, 1), 3)

    def test_complex(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(count_pairs([1, 2, 3, -2, -1], 5, 1), 2)
        self.assertEqual(count_pairs([10, 5, 2, 4, 1], 5, 9), 0)
        self.assertEqual(count_pairs([10, 5, 2, 4, 1], 5, -5), 1)
