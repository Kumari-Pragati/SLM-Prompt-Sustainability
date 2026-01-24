import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_even_Pair([1], 1), 0)
        self.assertEqual(find_even_Pair([0], 1), 0)

    def test_even_elements(self):
        self.assertEqual(find_even_Pair([0, 2, 4], 3), 2)

    def test_odd_elements(self):
        self.assertEqual(find_even_Pair([1, 3, 5], 3), 0)

    def test_mixed_even_odd_elements(self):
        self.assertEqual(find_even_Pair([0, 1, 2, 3, 4], 5), 3)

    def test_negative_numbers(self):
        self.assertEqual(find_even_Pair([-1, -2, -3], 3), 1)

    def test_duplicate_elements(self):
        self.assertEqual(find_even_Pair([0, 0, 2, 4], 4), 2)

    def test_large_numbers(self):
        self.assertEqual(find_even_Pair([1000000000000000000, 1000000000000000001], 2), 0)
