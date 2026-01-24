import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_sum_Pairs(self):
        self.assertEqual(sum_Pairs([1,2,3,4,5],5), 15)
        self.assertEqual(sum_Pairs([1,2,3,4,5,6],6), 21)
        self.assertEqual(sum_Pairs([1,2,3,4,5,6,7],7), 28)
        self.assertEqual(sum_Pairs([1,2,3,4,5,6,7,8],8), 36)
        self.assertEqual(sum_Pairs([1,2,3,4,5,6,7,8,9],9), 45)
        self.assertEqual(sum_Pairs([1,2,3,4,5,6,7,8,9,10],10), 55)

    def test_sum_Pairs_edge_cases(self):
        self.assertEqual(sum_Pairs([1],1), 0)
        self.assertEqual(sum_Pairs([1,2],2), 0)
        self.assertEqual(sum_Pairs([1,2,3],3), 0)
        self.assertEqual(sum_Pairs([1,2,3,4],4), 0)
        self.assertEqual(sum_Pairs([1,2,3,4,5],0), 0)
