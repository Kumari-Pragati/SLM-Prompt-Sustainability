import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(char_frequency('aabbbccc'), {'a': 2, 'b': 3, 'c': 3})

    def test_single_character(self):
        self.assertEqual(char_frequency('a'), {'a': 1})

    def test_empty_string(self):
        self.assertEqual(char_frequency(''), {})

    def test_case_sensitivity(self):
        self.assertNotEqual(char_frequency('Aa'), {'A': 1, 'a': 1})

    def test_whitespace(self):
        self.assertEqual(char_frequency(' '), {' ': 1})

    def test_special_characters(self):
        self.assertEqual(char_frequency('!@#$%^&*()'), {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1})
