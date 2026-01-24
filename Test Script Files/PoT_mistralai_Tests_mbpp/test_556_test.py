import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_Odd_Pair([1, 1, 2, 3, 4], 5), 1)
        self.assertEqual(find_Odd_Pair([4, 4, 4, 5, 6], 5), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_edge_case_all_same(self):
        self.assertEqual(find_Odd_Pair([1, 1, 1], 3), 0)

    def test_edge_case_all_even(self):
        self.assertEqual(find_Odd_Pair([2, 2, 2, 2], 4), 0)

    def test_edge_case_all_odd(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7], 4), 0)

    def test_corner_case_single_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 1)
