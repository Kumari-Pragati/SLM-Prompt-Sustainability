import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_sum_Pairs(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6], 6), 4)
        self.assertEqual(sum_Pairs([10, 20, 30, 40, 50], 5), 0)
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5, 6, 7], 7), 6)
        self.assertEqual(sum_Pairs([100, 200, 300, 400, 500], 5), 0)
