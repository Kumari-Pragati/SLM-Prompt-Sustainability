import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(string_to_list("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_whitespace_only(self):
        self.assertEqual(string_to_list("   "), [])

    def test_numbers_and_letters(self):
        self.assertEqual(string_to_list("123 abc"), ["123", "abc"])

    def test_special_characters(self):
        self.assertEqual(string_to_list("!@#$%^&*"), ["!@#$%^&*"])
