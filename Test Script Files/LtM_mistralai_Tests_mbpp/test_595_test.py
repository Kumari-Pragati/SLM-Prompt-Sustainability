import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_simple_same_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)

    def test_simple_identical_strings(self):
        self.assertEqual(min_Swaps("aaa", "aaa"), 0)

    def test_simple_different_strings(self):
        self.assertEqual(min_Swaps("abc", "acb"), 1)

    def test_simple_different_lengths(self):
        self.assertEqual(min_Swaps("abc", "a"), 2)

    def test_edge_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("", "a"), 1)
        self.assertEqual(min_Swaps("a", ""), 1)

    def test_edge_single_char_strings(self):
        self.assertEqual(min_Swaps("a", "b"), 1)
        self.assertEqual(min_Swaps("b", "a"), 1)

    def test_edge_alternating_chars(self):
        self.assertEqual(min_Swaps("abab", "baab"), 1)

    def test_edge_identical_ends_different_middles(self):
        self.assertEqual(min_Swaps("abcdabcd", "cdabcdabcd"), 2)

    def test_edge_identical_middles_different_ends(self):
        self.assertEqual(min_Swaps("abcdabcd", "cdababcd"), 4)

    def test_edge_case_one_char_different(self):
        self.assertEqual(min_Swaps("aabbcc", "aabbcce"), 1)

    def test_edge_case_one_char_different_in_middle(self):
        self.assertEqual(min_Swaps("aabbcc", "aabbccee"), 2)

    def test_edge_case_one_char_different_at_end(self):
        self.assertEqual(min_Swaps("aabbcc", "aabbccea"), 2)

    def test_edge_case_one_char_different_at_both_ends(self):
        self.assertEqual(min_Swaps("aabbcc", "bbaacc"), 4)
