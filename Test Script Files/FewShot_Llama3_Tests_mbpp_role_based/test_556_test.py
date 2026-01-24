import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_even_length_array(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4], 4), 0)

    def test_odd_length_array(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 1)

    def test_all_odd_array(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7, 9], 5), 4)

    def test_all_even_array(self):
        self.assertEqual(find_Odd_Pair([2, 4, 6, 8, 10], 5), 0)

    def test_mixed_array(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 2)
