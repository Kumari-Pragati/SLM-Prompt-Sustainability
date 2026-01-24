import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4], 4), 1)
        self.assertEqual(find_even_Pair([2, 2, 2, 4], 4), 2)
        self.assertEqual(find_even_Pair([1, 3, 5, 7], 4), 0)

    def test_edge_cases(self):
        self.assertEqual(find_even_Pair([], 0), 0)
        self.assertEqual(find_even_Pair([2], 1), 0)
        self.assertEqual(find_even_Pair([2, 2], 2), 1)
        self.assertEqual(find_even_Pair([2, 2, 2], 3), 2)
        self.assertEqual(find_even_Pair([2, 2, 2, 2], 4), 3)

    def test_complex(self):
        self.assertEqual(find_even_Pair([0, 1, 2, 3, 4], 5), 3)
        self.assertEqual(find_even_Pair([1, 3, 5, 7, 9], 5), 0)
        self.assertEqual(find_even_Pair([1, 3, 5, 7, 9, 11], 6), 1)
        self.assertEqual(find_even_Pair([1, 3, 5, 7, 9, 11, 13], 7), 2)
