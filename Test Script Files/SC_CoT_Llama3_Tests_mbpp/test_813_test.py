import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_typical_string(self):
        self.assertEqual(string_length("Hello, World!"), 13)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_multiple_spaces(self):
        self.assertEqual(string_length("   "), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_length(123)

    def test_string_with_newline(self):
        self.assertEqual(string_length("Hello\nWorld!"), 12)

    def test_string_with_tabs(self):
        self.assertEqual(string_length("Hello\tWorld!"), 12)

    def test_string_with_multiple_newlines(self):
        self.assertEqual(string_length("Hello\n\nWorld!"), 13)
