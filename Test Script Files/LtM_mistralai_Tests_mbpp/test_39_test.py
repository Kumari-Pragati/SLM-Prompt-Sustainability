import unittest
from mbpp_39_code import rearange_string

class TestRearrangeString(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(rearrange_string("aaabbc"), "abcbab")

    def test_single_char(self):
        self.assertEqual(rearrange_string("a"), "a")

    def test_edge_case_empty_string(self):
        self.assertEqual(rearrange_string(""), "")

    def test_edge_case_single_char_repeat(self):
        self.assertEqual(rearrange_string("aaa"), "aa")

    def test_edge_case_max_length(self):
        self.assertEqual(rearrange_string("a" * 1001), "a" * 1001)

    def test_edge_case_min_length(self):
        self.assertEqual(rearrange_string(""), "")

    def test_edge_case_only_one_char_different(self):
        self.assertEqual(rearrange_string("abab"), "abab")

    def test_edge_case_only_one_char_same(self):
        self.assertEqual(rearrange_string("aa"), "aa")

    def test_edge_case_only_two_chars(self):
        self.assertEqual(rearrange_string("aaab"), "aab")
