import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 2, 4, 3, 5], 7), 2)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5), 4)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6], 6, 0), 0)
        self.assertEqual(count_Pairs([], 0), 0)

    def test_count_Pairs_edge_cases(self):
        self.assertEqual(count_Pairs([1], 1), 0)
        self.assertEqual(count_Pairs([1, 1], 2, 1), 1)
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 5), 5)
