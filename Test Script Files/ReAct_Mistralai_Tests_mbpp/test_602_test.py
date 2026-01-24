import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_repeated_char(""), "None")

    def test_single_char_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(first_repeated_char(char), char)

    def test_string_with_no_repeated_chars(self):
        self.assertEqual(first_repeated_char("zyxwvutsrqponmlkjihgfedcba"), "None")

    def test_string_with_repeated_chars_at_beginning(self):
        self.assertEqual(first_repeated_char("aaab"), "a")

    def test_string_with_repeated_chars_in_middle(self):
        self.assertEqual(first_repeated_char("abcabc"), "a")

    def test_string_with_repeated_chars_at_end(self):
        self.assertEqual(first_repeated_char("xyzxyz"), "x")

    def test_string_with_multiple_repeated_chars(self):
        self.assertEqual(first_repeated_char("aaabbc"), "a")

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(first_repeated_char(" aabbc def "), "a")

    def test_string_with_non_alphabetic_characters(self):
        self.assertEqual(first_repeated_char("123aABC!@#$%"), "None")
