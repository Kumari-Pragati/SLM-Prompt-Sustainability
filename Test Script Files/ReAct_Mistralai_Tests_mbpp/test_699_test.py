import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("", "a"), 1)
        self.assertEqual(min_Swaps("a", ""), 1)

    def test_single_character_strings(self):
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("a", "b"), 1)

    def test_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abcd", "abcd"), 0)

    def test_different_lengths(self):
        self.assertEqual(min_Swaps("abc", "abcd"), 1)
        self.assertEqual(min_Swaps("abcd", "abc"), 1)

    def test_alternating_characters(self):
        self.assertEqual(min_Swaps("abcd", "acdb"), 1)
        self.assertEqual(min_Swaps("acdb", "abcd"), 1)

    def test_not_possible_case(self):
        self.assertEqual(min_Swaps("abcd", "abca"), "Not Possible")

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            min_Swaps(1, 2)
        with self.assertRaises(TypeError):
            min_Swaps("abc", 123)
