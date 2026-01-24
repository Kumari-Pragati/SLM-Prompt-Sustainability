import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_empty_string(self):
        self.assertDictEqual(char_frequency(''), {})

    def test_single_character(self):
        self.assertDictEqual(char_frequency('a'), {'a': 1})

    def test_multiple_characters(self):
        self.assertDictEqual(char_frequency('abc'), {'a': 1, 'b': 1, 'c': 1})

    def test_case_sensitivity(self):
        self.assertDictEqual(char_frequency('ABC'), {'A': 1, 'B': 1, 'C': 1})

    def test_whitespace(self):
        self.assertDictEqual(char_frequency(' a b c '), {' ': 2, 'a': 1, 'b': 1, 'c': 1})

    def test_special_characters(self):
        self.assertDictEqual(char_frequency('!@#$%^&*()'),
                             {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1})

    def test_long_string(self):
        long_string = 'x' * 1000
        self.assertGreater(len(char_frequency(long_string)), 999)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            char_frequency(123)
