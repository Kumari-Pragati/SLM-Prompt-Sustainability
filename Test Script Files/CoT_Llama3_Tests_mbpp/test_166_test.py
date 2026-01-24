import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_even_Pair([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_even_Pair([1], 1), 0)

    def test_two_elements_array(self):
        self.assertEqual(find_even_Pair([1, 2], 2), 1)

    def test_three_elements_array(self):
        self.assertEqual(find_even_Pair([1, 2, 3], 3), 2)

    def test_large_array(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(find_even_Pair([-1, -2, 3, 4, 5, 6], 6), 3)

    def test_non_integer_numbers(self):
        self.assertEqual(find_even_Pair([1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 6), 0)

    def test_array_with_duplicates(self):
        self.assertEqual(find_even_Pair([1, 2, 2, 3, 4, 5], 6), 2)
