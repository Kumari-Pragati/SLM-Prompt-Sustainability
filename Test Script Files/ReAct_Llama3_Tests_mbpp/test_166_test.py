import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_even_Pair([1], 1), 0)

    def test_two_elements_array(self):
        self.assertEqual(find_even_Pair([1, 2], 2), 1)

    def test_even_pair_array(self):
        self.assertEqual(find_even_Pair([1, 2, 4, 5, 6], 5), 2)

    def test_odd_pair_array(self):
        self.assertEqual(find_even_Pair([1, 3, 5, 7, 9], 5), 0)

    def test_large_array(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 4)
