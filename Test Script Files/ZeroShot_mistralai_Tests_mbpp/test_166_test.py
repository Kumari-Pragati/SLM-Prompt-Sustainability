import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_even_Pair([1], 1), 0)
        self.assertEqual(find_even_Pair([2], 1), 0)

    def test_single_even_element(self):
        self.assertEqual(find_even_Pair([2], 1), 0)
        self.assertEqual(find_even_Pair([4], 1), 0)

    def test_single_odd_element(self):
        self.assertEqual(find_even_Pair([1], 1), 0)
        self.assertEqual(find_even_Pair([3], 1), 0)

    def test_two_elements(self):
        self.assertEqual(find_even_Pair([1, 2], 2), 1)
        self.assertEqual(find_even_Pair([2, 2], 2), 1)
        self.assertEqual(find_even_Pair([1, 3], 2), 0)

    def test_multiple_elements(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4], 4), 2)
        self.assertEqual(find_even_Pair([1, 2, 4, 4], 4), 2)
        self.assertEqual(find_even_Pair([1, 1, 3, 5], 4), 0)
