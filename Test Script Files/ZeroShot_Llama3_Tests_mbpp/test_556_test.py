import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_find_Odd_Pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 2)
        self.assertEqual(find_Odd_Pair([1, 1, 1, 1, 1, 1], 6, 0), 0)
        self.assertEqual(find_Odd_Pair([], 0), 0)
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 4)
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16, 0), 8)
