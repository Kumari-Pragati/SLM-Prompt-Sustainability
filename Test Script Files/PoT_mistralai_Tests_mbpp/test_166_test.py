import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_even_Pair([2, 2, 2, 3, 4], 5), 2)
        self.assertEqual(find_even_Pair([1, 1, 2, 3, 4], 5), 1)

    def test_edge_case_empty(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_even_Pair([1], 1), 0)

    def test_edge_case_single_pair(self):
        self.assertEqual(find_even_Pair([1, 2], 2), 1)

    def test_corner_case_all_even(self):
        self.assertEqual(find_even_Pair([2, 2, 2, 2], 4), 3)

    def test_corner_case_all_odd(self):
        self.assertEqual(find_even_Pair([1, 3, 5, 7], 4), 0)
