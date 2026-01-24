import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), "Not Possible")

    def test_single_character_strings(self):
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("a", "b"), 1)
        self.assertEqual(min_Swaps("b", "a"), 1)

    def test_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abcd", "abcd"), 0)

    def test_non_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abd"), 1)
        self.assertEqual(min_Swaps("abcd", "abce"), 2)
        self.assertEqual(min_Swaps("abc", "def"), 3)

    def test_strings_with_repeated_characters(self):
        self.assertEqual(min_Swaps("aa", "aa"), 0)
        self.assertEqual(min_Swaps("aa", "ab"), 1)
        self.assertEqual(min_Swaps("ab", "aa"), 1)
