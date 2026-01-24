import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character_string(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_no_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 3)

    def test_repeating_subsequence_with_spaces(self):
        self.assertEqual(find_longest_repeating_subseq("abc abc"), 3)

    def test_repeating_subsequence_with_punctuation(self):
        self.assertEqual(find_longest_repeating_subseq("abc!abc"), 3)

    def test_repeating_subsequence_with_numbers(self):
        self.assertEqual(find_longest_repeating_subseq("abc123abc"), 3)
