import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_two_elements_list(self):
        self.assertEqual(find_Odd_Pair([1, 2], 2), 0)

    def test_odd_pair_in_list(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 1)

    def test_multiple_odd_pairs_in_list(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 3)

    def test_large_list(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 7)
