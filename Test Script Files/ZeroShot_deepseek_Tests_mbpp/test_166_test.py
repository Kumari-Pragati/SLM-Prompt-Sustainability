import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_even_pair(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4], 4), 2)
        self.assertEqual(find_even_Pair([1, 3, 5, 7], 4), 0)
        self.assertEqual(find_even_Pair([2, 4, 6, 8], 4), 6)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 20)
