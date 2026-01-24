import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_single_element_input(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_two_elements_input(self):
        self.assertEqual(find_Odd_Pair([1, 2], 2), 0)

    def test_odd_pair_input(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5], 3), 1)

    def test_even_pair_input(self):
        self.assertEqual(find_Odd_Pair([2, 4, 6], 3), 0)

    def test_large_input(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7, 9, 11, 13, 15], 8), 4)

    def test_negative_input(self):
        self.assertEqual(find_Odd_Pair([-1, -3, -5], 3), 0)

    def test_mixed_input(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 4)
