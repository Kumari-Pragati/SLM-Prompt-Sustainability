import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_empty_string(self):
        self.assertDictEqual(char_frequency(''), {})

    def test_single_character(self):
        self.assertDictEqual(char_frequency('a'), {'a': 1})

    def test_multiple_characters(self):
        self.assertDictEqual(char_frequency('abc'), {'a': 1, 'b': 1, 'c': 1})

    def test_repeated_characters(self):
        self.assertDictEqual(char_frequency('aaa'), {'a': 3})

    def test_special_characters(self):
        self.assertDictEqual(char_frequency('!@#$%^&*()'), {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1})

    def test_whitespace(self):
        self.assertDictEqual(char_frequency('  '), {' ': 2})

    def test_unicode(self):
        self.assertDictEqual(char_frequency('\u00E9'), {'é': 1})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            char_frequency(123)
