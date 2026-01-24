import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 4)

    def test_edge_case_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_edge_case_two_characters(self):
        self.assertEqual(find_longest_repeating_subseq("aa"), 2)

    def test_edge_case_three_characters(self):
        self.assertEqual(find_longest_repeating_subseq("aba"), 3)

    def test_edge_case_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("ababab"), 4)

    def test_edge_case_non_repeating_subsequence(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 3)

    def test_edge_case_repeating_subsequence_at_end(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 4)

    def test_edge_case_repeating_subsequence_at_start(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 4)

    def test_edge_case_repeating_subsequence_at_middle(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 4)
