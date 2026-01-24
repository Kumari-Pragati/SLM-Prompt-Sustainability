import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_string("hello world", 2), ["he", "ll", "o ", "wo", "rl", "rd"])

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_string("", 2), [])

    def test_edge_case_single_character_string(self):
        self.assertEqual(extract_string("a", 1), ["a"])

    def test_edge_case_single_character_string_with_spaces(self):
        self.assertEqual(extract_string("a b", 1), ["a", "b"])

    def test_edge_case_empty_string_with_spaces(self):
        self.assertEqual(extract_string("   ", 1), [])

    def test_edge_case_string_with_spaces_and_newlines(self):
        self.assertEqual(extract_string("hello\nworld", 2), ["he", "ll", "\n", "wo", "rl", "rd"])

    def test_edge_case_string_with_spaces_and_newlines_and_tabs(self):
        self.assertEqual(extract_string("hello\nworld\tabc", 2), ["he", "ll", "\n", "wo", "rl", "\t", "ab", "c"])

    def test_edge_case_string_with_spaces_and_newlines_and_tabs_and_commas(self):
        self.assertEqual(extract_string("hello\nworld\tabc,def", 2), ["he", "ll", "\n", "wo", "rl", "\t", "ab", "c", ",", "de", "f"])

    def test_edge_case_string_with_spaces_and_newlines_and_tabs_and_commas_and_colons(self):
        self.assertEqual(extract_string("hello\nworld\tabc,def:ghi", 2), ["he", "ll", "\n", "wo", "rl", "\t", "ab", "c", ",", "de", "f", ":", "gh", "i"])
