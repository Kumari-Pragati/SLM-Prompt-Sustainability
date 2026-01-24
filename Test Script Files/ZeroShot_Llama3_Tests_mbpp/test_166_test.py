import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_find_even_Pair(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6], 6), 3)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6, 7], 7), 3)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6, 7, 8], 8, 4), 4)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 5), 4)
