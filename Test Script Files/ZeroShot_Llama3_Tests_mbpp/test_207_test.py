import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character_string(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 0)

    def test_no_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("aba"), 2)

    def test_repeating_subsequence_with_spaces(self):
        self.assertEqual(find_longest_repeating_subseq("a b a"), 2)

    def test_repeating_subsequence_with_punctuation(self):
        self.assertEqual(find_longest_repeating_subseq("a,b,c!"), 0)

    def test_repeating_subsequence_with_numbers(self):
        self.assertEqual(find_longest_repeating_subseq("123456"), 0)

    def test_repeating_subsequence_with_special_characters(self):
        self.assertEqual(find_longest_repeating_subseq("a!b@c"), 0)
