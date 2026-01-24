import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_repeated_char(""), "None")

    def test_single_char_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(first_repeated_char(char), char)

    def test_no_repeated_char_string(self):
        self.assertEqual(first_repeated_char("zyxwvutsrqponmlkjihgfedcba"), "None")

    def test_repeated_char_string(self):
        self.assertEqual(first_repeated_char("aaabbbccc"), "a")

    def test_repeated_char_at_end_string(self):
        self.assertEqual(first_repeated_char("abcabc"), "c")

    def test_repeated_char_in_middle_string(self):
        self.assertEqual(first_repeated_char("aaaabbccc"), "a")
