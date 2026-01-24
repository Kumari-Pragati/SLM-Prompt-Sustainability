import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4], 4), 6)
        self.assertEqual(count_Pairs([1, 1, 1, 1], 4), 0)
        self.assertEqual(count_Pairs([10, 20, 30, 40], 4), 6)
        self.assertEqual(count_Pairs([1, 2, 2, 1], 4), 2)
        self.assertEqual(count_Pairs([5, 5, 5, 5, 5], 5), 0)
