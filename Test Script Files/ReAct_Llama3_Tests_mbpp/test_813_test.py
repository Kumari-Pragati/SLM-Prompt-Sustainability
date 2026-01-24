import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(string_length("hello"), 5)

    def test_spaces(self):
        self.assertEqual(string_length("   "), 3)

    def test_punctuation(self):
        self.assertEqual(string_length("Hello, World!"), 13)

    def test_newline(self):
        self.assertEqual(string_length("Hello\nWorld"), 11)

    def test_tabs(self):
        self.assertEqual(string_length("Hello\tWorld"), 11)

    def test_mixed_characters(self):
        self.assertEqual(string_length("Hello, World! 123"), 19)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_length(123)
