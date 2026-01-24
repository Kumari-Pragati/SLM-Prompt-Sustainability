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
        self.assertEqual(find_Odd_Pair([1, 2, 3, 5], 4), 1)

    def test_odd_length_list_no_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3], 3), 0)

    def test_odd_length_list_with_odd_pair(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 5], 4), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Odd_Pair([-1, -2, 3], 3), 0)

    def test_duplicate_numbers(self):
        self.assertEqual(find_Odd_Pair([1, 1, 3], 3), 0)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            find_Odd_Pair(None, 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            find_Odd_Pair("string", 0)
