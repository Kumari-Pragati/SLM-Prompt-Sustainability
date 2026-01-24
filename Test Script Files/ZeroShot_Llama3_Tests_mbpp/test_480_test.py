import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), None)

    def test_single_char_string(self):
        self.assertEqual(get_max_occuring_char("a"), "a")

    def test_multiple_char_string(self):
        self.assertEqual(get_max_occuring_char("abab"), "a")

    def test_string_with_spaces(self):
        self.assertEqual(get_max_occuring_char("a b c"), "a")

    def test_string_with_punctuation(self):
        self.assertEqual(get_max_occuring_char("Hello, World!"), "o")

    def test_string_with_digits(self):
        self.assertEqual(get_max_occuring_char("1234567890"), "1")

    def test_string_with_special_chars(self):
        self.assertEqual(get_max_occuring_char("!,@#$%^&*()"), "!")

    def test_string_with_multiple_max_occuring_chars(self):
        self.assertEqual(get_max_occuring_char("aaaabbbcc"), "a")

    def test_string_with_no_max_occuring_chars(self):
        self.assertEqual(get_max_occuring_char("abcdefghijklmnopqrstuvwxyz"), None)
