import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_single_lowercase_char(self):
        self.assertEqual(remove_lowercase("a"), "")

    def test_multiple_lowercase_chars(self):
        self.assertEqual(remove_lowercase("abc"), "")

    def test_mixed_case_string(self):
        self.assertEqual(remove_lowercase("AbC"), "AbC")

    def test_string_with_uppercase_chars(self):
        self.assertEqual(remove_lowercase("ABC"), "ABC")

    def test_string_with_digits(self):
        self.assertEqual(remove_lowercase("123"), "123")

    def test_string_with_punctuation(self):
        self.assertEqual(remove_lowercase("Hello, World!"), "Hello, World!")

    def test_string_with_spaces(self):
        self.assertEqual(remove_lowercase("Hello World"), "Hello World")

    def test_string_with_newlines(self):
        self.assertEqual(remove_lowercase("Hello\nWorld"), "Hello\nWorld")
