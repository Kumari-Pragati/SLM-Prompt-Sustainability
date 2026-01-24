import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)

    def test_single_element(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_all_even(self):
        self.assertEqual(find_Odd_Pair([2, 4, 6, 8], 4), 0)

    def test_all_odd(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7], 4), 6)

    def test_mixed_numbers(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 10)

    def test_negative_numbers(self):
        self.assertEqual(find_Odd_Pair([-1, -2, -3, -4, -5], 5), 2)

    def test_large_numbers(self):
        self.assertEqual(find_Odd_Pair([1000000001, 1000000002, 1000000003], 3), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Odd_Pair("not a list", 5)
