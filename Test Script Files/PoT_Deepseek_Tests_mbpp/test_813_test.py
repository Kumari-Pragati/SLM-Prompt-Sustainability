import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_length("Hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_whitespace_string(self):
        self.assertEqual(string_length(" "), 1)

    def test_long_string(self):
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_string_with_special_characters(self):
        self.assertEqual(string_length("!@#$%^&*()"), 9)

    def test_string_with_numbers(self):
        self.assertEqual(string_length("1234567890"), 10)
