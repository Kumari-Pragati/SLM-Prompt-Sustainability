import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_remove_whitespaces_from_single_word(self):
        self.assertEqual(remove_whitespaces("Hello"), "Hello")

    def test_remove_whitespaces_from_multiple_words(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_remove_whitespaces_from_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("   Hello   World   "), "HelloWorld")

    def test_remove_whitespaces_from_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_remove_whitespaces_from_string_with_tabs(self):
        self.assertEqual(remove_whitespaces("\tHello\tWorld"), "HelloWorld")
