import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_replace_single_char(self):
        self.assertEqual(replace("a", "x"), "xx")

    def test_replace_multiple_chars(self):
        self.assertEqual(replace("aa", "x"), "xxxx")

    def test_replace_empty_string(self):
        self.assertEqual(replace("", "x"), "")

    def test_replace_single_char_with_longer_pattern(self):
        self.assertEqual(replace("x", "xx"), "xxxx")

    def test_replace_string_with_only_matching_chars(self):
        self.assertEqual(replace("aaaa", "a"), "aaaa")

    def test_replace_string_with_non_matching_chars(self):
        self.assertEqual(replace("abcd", "a"), "abcd")

    def test_replace_string_with_only_matching_chars_edge_case(self):
        self.assertEqual(replace("a", "aa"), "aaa")

    def test_replace_string_with_non_matching_chars_edge_case(self):
        self.assertEqual(replace("z", "aa"), "zz")
