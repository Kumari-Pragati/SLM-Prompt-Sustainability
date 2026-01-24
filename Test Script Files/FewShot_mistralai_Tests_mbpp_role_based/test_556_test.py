import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_even_length_list_no_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4], 4), 0)

    def test_even_length_list_with_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 1)

    def test_odd_length_list_no_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 0)

    def test_odd_length_list_with_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7], 7), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Odd_Pair([-1, -2, -3, -4], 4), 0)

    def test_zero(self):
        self.assertEqual(find_Odd_Pair([0, 0, 0], 3), 0)
