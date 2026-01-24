import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_valid_input_3_to_5_chars(self):
        self.assertListEqual(find_char("abc"), ["abc"])
        self.assertListEqual(find_char("abcd"), ["abcd"])
        self.assertListEqual(find_char("abcde"), ["abc", "de"])

    def test_valid_input_less_than_3_chars(self):
        self.assertListEqual(find_char("ab"), [])
        self.assertListEqual(find_char("abc"), ["abc"])
        self.assertListEqual(find_char("abcd"), ["abcd"])

    def test_valid_input_more_than_5_chars(self):
        self.assertListEqual(find_char("abcdefg"), ["abc", "def"])
        self.assertListEqual(find_char("abcdefgh"), ["abc", "def", "gh"])
        self.assertListEqual(find_char("abcdefghi"), ["abc", "def", "ghi"])

    def test_empty_string(self):
        self.assertListEqual(find_char(""), [])

    def test_single_char_string(self):
        self.assertListEqual(find_char("a"), [])
        self.assertListEqual(find_char("b"), [])
        self.assertListEqual(find_char("c"), [])
