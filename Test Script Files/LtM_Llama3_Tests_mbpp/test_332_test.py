import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_single_char_string(self):
        self.assertEqual(char_frequency("a"), {"a": 1})

    def test_multiple_char_string(self):
        self.assertEqual(char_frequency("abc"), {"a": 1, "b": 1, "c": 1})

    def test_repeated_chars(self):
        self.assertEqual(char_frequency("aaabbb"), {"a": 3, "b": 3})

    def test_non_ascii_chars(self):
        self.assertEqual(char_frequency("abcé"), {"a": 1, "b": 1, "c": 1, "é": 1})

    def test_empty_string_input(self):
        with self.assertRaises(TypeError):
            char_frequency(None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            char_frequency(123)

    def test_non_string_input_with_conversion(self):
        with self.assertRaises(TypeError):
            char_frequency(int("123"))
