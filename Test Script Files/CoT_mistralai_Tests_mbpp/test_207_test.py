import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_longest_repeating_subseq(char), 1)

    def test_palindrome(self):
        self.assertEqual(find_longest_repeating_subseq("level"), 5)
        self.assertEqual(find_longest_repeating_subseq("madam"), 4)

    def test_repeating_sequence(self):
        self.assertEqual(find_longest_repeating_subseq("ababab"), 4)
        self.assertEqual(find_longest_repeating_subseq("aabbaa"), 3)

    def test_long_sequence(self):
        self.assertEqual(find_longest_repeating_subseq("a" * 100), 100)

    def test_different_characters(self):
        self.assertEqual(find_longest_repeating_subseq("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_longest_repeating_subseq, 123)
        self.assertRaises(TypeError, find_longest_repeating_subseq, [])
