import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_longest_repeating_subseq(char), 1)

    def test_simple_strings(self):
        self.assertEqual(find_longest_repeating_subseq("abab"), 2)
        self.assertEqual(find_longest_repeating_subseq("abcdabcd"), 4)
        self.assertEqual(find_longest_repeating_subseq("aababcdabcd"), 5)
        self.assertEqual(find_longest_repeating_subseq("aababcdabcdabcd"), 6)

    def test_complex_strings(self):
        self.assertEqual(find_longest_repeating_subseq("banana"), 3)
        self.assertEqual(find_longest_repeating_subseq("apple"), 1)
        self.assertEqual(find_longest_repeating_subseq("appelle"), 2)
        self.assertEqual(find_longest_repeating_subseq("appellee"), 3)
        self.assertEqual(find_longest_repeating_subseq("appelleee"), 4)
