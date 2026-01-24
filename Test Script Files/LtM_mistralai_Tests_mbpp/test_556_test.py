import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_Odd_Pair([2, 4, 6, 8, 10], 5), 1)
        self.assertEqual(find_Odd_Pair([1, 1, 2, 3, 4], 5), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)
        self.assertEqual(find_Odd_Pair([1], 1), 0)
        self.assertEqual(find_Odd_Pair([1, 1], 2), 0)
        self.assertEqual(find_Odd_Pair([1, 1, 1], 3), 0)
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 3)
        self.assertEqual(find_Odd_Pair([2147483647, 2147483647], 2), 0)

    def test_complex(self):
        self.assertEqual(find_Odd_Pair([1, 2, 4, 7, 10, 11, 12, 13, 14, 15], 10), 2)
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], 16), 0)
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33], 17), 1)
