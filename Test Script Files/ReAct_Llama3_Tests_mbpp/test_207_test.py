import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_single_character_string(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_no_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 1)

    def test_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 3)

    def test_repeating_subsequence_with_gaps(self):
        self.assertEqual(find_longest_repeating_subseq("abcbadcb"), 4)

    def test_repeating_subsequence_with_gaps_and_non_repeating_chars(self):
        self.assertEqual(find_longest_repeating_subseq("abcbadcbxyz"), 4)

    def test_repeating_subsequence_with_gaps_and_non_repeating_chars_and_duplicates(self):
        self.assertEqual(find_longest_repeating_subseq("abcbadcbxyzabc"), 5)

    def test_repeating_subsequence_with_gaps_and_non_repeating_chars_and_duplicates_and_duplicates(self):
        self.assertEqual(find_longest_repeating_subseq("abcbadcbxyzabcabc"), 6)
