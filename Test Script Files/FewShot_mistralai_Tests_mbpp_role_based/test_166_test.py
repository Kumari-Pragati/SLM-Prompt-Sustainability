import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_even_Pair([1], 1), 0)

    def test_single_even_element_list(self):
        self.assertEqual(find_even_Pair([2], 1), 1)

    def test_single_odd_element_list(self):
        self.assertEqual(find_even_Pair([1], 1), 0)

    def test_multiple_even_elements_list(self):
        self.assertEqual(find_even_Pair([2, 4, 6], 3), 3)

    def test_multiple_odd_elements_list(self):
        self.assertEqual(find_even_Pair([1, 3, 5], 3), 0)

    def test_mixed_even_odd_elements_list(self):
        self.assertEqual(find_even_Pair([2, 1, 4, 3, 6], 5), 3)

    def test_list_longer_than_N(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6], 3), 3)

    def test_list_shorter_than_N(self):
        self.assertEqual(find_even_Pair([1, 2], 3), 0)
