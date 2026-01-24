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

    def test_reversed_palindrome(self):
        self.assertEqual(find_longest_repeating_subseq("madam"), 4)

    def test_repeated_characters(self):
        self.assertEqual(find_longest_repeating_subseq("aaa"), 3)

    def test_repeated_characters_with_different_characters(self):
        self.assertEqual(find_longest_repeating_subseq("ababab"), 3)

    def test_long_string(self):
        self.assertEqual(find_longest_repeating_subseq("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_string_with_repeated_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("banana"), 3)

    def test_string_with_multiple_repeated_subsequences(self):
        self.assertEqual(find_longest_repeating_subseq("bananabana"), 4)

    def test_string_with_no_repeated_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abcdefghijklmnopqrstuvwxyz1234567890"), 0)
