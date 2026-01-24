import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("world"), "World")

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_whitespace_only(self):
        self.assertEqual(capitalize_first_last_letters("   "), "   ")

    def test_punctuation_at_start(self):
        self.assertEqual(capitalize_first_last_letters("!hello world"), "!Hello World")

    def test_punctuation_at_end(self):
        self.assertEqual(capitalize_first_last_letters("hello world!"), "Hello World!")

    def test_punctuation_in_middle(self):
        self.assertEqual(capitalize_first_last_letters("hello, world!"), "Hello, World!")

    def test_multiple_spaces(self):
        self.assertEqual(capitalize_first_last_letters("  hello world  "), "  Hello World  ")

    def test_all_uppercase(self):
        self.assertEqual(capitalize_first_last_letters("HELLO WORLD"), "Hello World")

    def test_all_lowercase(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")

    def test_all_numbers(self):
        self.assertEqual(capitalize_first_last_letters("1234567890"), "1234567890")
