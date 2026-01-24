import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_repeating_subseq("aabcb"), 2)

    def test_typical_case_with_repeating_chars(self):
        self.assertEqual(find_longest_repeating_subseq("aabb"), 2)

    def test_typical_case_with_same_chars(self):
        self.assertEqual(find_longest_repeating_subseq("aaaa"), 2)

    def test_edge_case_with_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_edge_case_with_single_char(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 0)

    def test_error_case_with_none_input(self):
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(None)
