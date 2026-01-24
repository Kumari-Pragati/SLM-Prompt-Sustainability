import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4], 4), 3)
        self.assertEqual(count_Pairs([5, 5, 6, 7], 4), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Pairs([], 0), 0)
        self.assertEqual(count_Pairs([1], 1), 0)
        self.assertEqual(count_Pairs([1, 1], 2), 1)
        self.assertEqual(count_Pairs([1, 1, 1], 3), 2)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 5], 6), 4)

    def test_complex(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 4, 4, 5], 8), 5)
        self.assertEqual(count_Pairs([1, 1, 1, 2, 2, 3, 4, 4, 5], 9), 6)
