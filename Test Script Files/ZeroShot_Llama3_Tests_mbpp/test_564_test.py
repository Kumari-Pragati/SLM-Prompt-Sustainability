import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,3,4,5],5), 4)
        self.assertEqual(count_Pairs([1,1,1,1,1],5), 0)
        self.assertEqual(count_Pairs([1,2,3,4,5,5],6), 4)
        self.assertEqual(count_Pairs([1,2,3,4,5,5,5],6, 1), 1)
        self.assertEqual(count_Pairs([],0), 0)
        self.assertEqual(count_Pairs([1],1), 0)
        self.assertEqual(count_Pairs([1,1],2), 0)
        self.assertEqual(count_Pairs([1,2,3,4,5,6,7,8,9,10],10), 9)
