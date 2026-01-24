import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_single_character_string(self):
        self.assertEqual(string_length('a'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(string_length('abc'), 3)

    def test_long_string(self):
        self.assertEqual(string_length('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_string_with_whitespace(self):
        self.assertEqual(string_length('hello world'), 11)
