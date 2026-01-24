import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_simple_input(self):
        self.assertListEqual(find_char("HelloWorld"), ["Hello", "World"])

    def test_min_length(self):
        self.assertListEqual(find_char("abc"), ["abc"])

    def test_max_length(self):
        self.assertListEqual(find_char("abcdefg"), ["abc", "def", "g"])

    def test_edge_case_min_length(self):
        self.assertListEqual(find_char("ab"), [])

    def test_edge_case_max_length(self):
        self.assertListEqual(find_char("abcdefghij"), ["abc", "def", "ghi", "j"])

    def test_special_characters(self):
        self.assertListEqual(find_char("!HelloWorld$"), [])

    def test_empty_string(self):
        self.assertListEqual(find_char(""), [])

    def test_whitespace_only(self):
        self.assertListEqual(find_char("   "), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_char(123)
