import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 5), 2)
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5), 4)
        self.assertEqual(count_Pairs([], 0), 0)
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 1), 0)
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 6), 3)
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 0), 0)
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], -1), 0)

    def test_complex(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3, 4, 4, 4, 5], 10), 5)
        self.assertEqual(count_Pairs([0, 0, 0, 1, 1, 1, 1, 2, 2, 2], 10), 4)
        self.assertEqual(count_Pairs([-1, -1, 0, 0, 1, 1, 1, 2, 2, 2], 10), 3)
