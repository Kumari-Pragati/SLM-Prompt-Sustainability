import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_single_character(self):
        self.assertEqual(char_frequency("a"), {"a": 1})

    def test_multiple_characters(self):
        self.assertEqual(char_frequency("abc"), {"a": 1, "b": 1, "c": 1})

    def test_repeated_characters(self):
        self.assertEqual(char_frequency("aaabbb"), {"a": 3, "b": 3})

    def test_spaces_and_punctuation(self):
        self.assertEqual(char_frequency("Hello, World!"), {"H": 1, "e": 1, "l": 3, "o": 2, ",": 1, "W": 1, "r": 1, "d": 1, "!": 1})

    def test_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello, World! à"), {"H": 1, "e": 1, "l": 3, "o": 2, ",": 1, "W": 1, "r": 1, "d": 1, "!": 1, "à": 1})

    def test_empty_string_with_non_ascii_characters(self):
        self.assertEqual(char_frequency(""), {})

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            char_frequency(123)
