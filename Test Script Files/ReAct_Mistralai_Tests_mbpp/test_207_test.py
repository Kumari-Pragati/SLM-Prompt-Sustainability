import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_longest_repeating_subseq(char), 1)

    def test_palindrome(self):
        self.assertEqual(find_longest_repeating_subseq("level"), 5)
        self.assertEqual(find_longest_repeating_subseq("madam"), 4)

    def test_anagrams(self):
        self.assertEqual(find_longest_repeating_subseq("listen"), 4)
        self.assertEqual(find_longest_repeating_subseq("silent"), 4)

    def test_reversed_string(self):
        self.assertEqual(find_longest_repeating_subseq("abcdefg"), 1)
        self.assertEqual(find_longest_repeating_subseq("gfedcba"), 6)

    def test_case_insensitive(self):
        self.assertEqual(find_longest_repeating_subseq("aBcDeFgHiJkLmNoPqRsTuVwXyZ"), 32)

    def test_long_strings(self):
        self.assertEqual(find_longest_repeating_subseq("a" * 100), 100)
        self.assertEqual(find_longest_repeating_subseq("a" * 101 + "b"), 100)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(123)
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(None)
        with self.assertRaises(ValueError):
            find_longest_repeating_subseq("")
