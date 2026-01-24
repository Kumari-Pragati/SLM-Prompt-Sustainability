import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(remove_char("HelloWorld"), "HelloWorld")

    def test_string_with_spaces(self):
        self.assertEqual(remove_char("Hello World"), "HelloWorld")

    def test_string_with_numbers(self):
        self.assertEqual(remove_char("Hello123World"), "HelloWorld")

    def test_string_with_special_characters(self):
        self.assertEqual(remove_char("Hello@World"), "HelloWorld")

    def test_string_with_underscores(self):
        self.assertEqual(remove_char("Hello_World"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_char(""), "")

    def test_single_character_string(self):
        self.assertEqual(remove_char("a"), "a")

    def test_string_with_only_whitespace(self):
        self.assertEqual(remove_char("   "), "")

    def test_string_with_only_non_alphanumeric_characters(self):
        self.assertEqual(remove_char("!@#$%^&*()_+-="), "")
