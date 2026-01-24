import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_single_char_string(self):
        self.assertEqual(char_frequency("a"), {'a': 1})

    def test_multiple_char_string(self):
        self.assertEqual(char_frequency("abc"), {'a': 1, 'b': 1, 'c': 1})

    def test_string_with_duplicates(self):
        self.assertEqual(char_frequency("aaabbb"), {'a': 3, 'b': 3})

    def test_string_with_spaces(self):
        self.assertEqual(char_frequency("hello world"), {'h': 1, 'e': 1, 'l': 3, 'o': 2,'': 1, 'w': 1, 'r': 1, 'd': 1})

    def test_string_with_punctuation(self):
        self.assertEqual(char_frequency("Hello, world!"), {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ',': 1,'': 1, 'r': 1, 'd': 1, '!': 1})
