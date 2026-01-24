import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(char_frequency('aabbc'), {'a': 2, 'b': 2, 'c': 1})

    def test_single_char(self):
        self.assertEqual(char_frequency('x'), {'x': 1})

    def test_empty_string(self):
        self.assertEqual(char_frequency(''), {})

    def test_case_sensitivity(self):
        self.assertNotEqual(char_frequency('Aa'), {'A': 1, 'a': 1})

    def test_whitespace(self):
        self.assertEqual(char_frequency('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_numeric_chars(self):
        self.assertEqual(char_frequency('123123'), {'1': 2, '2': 2, '3': 2})

    def test_special_chars(self):
        self.assertEqual(char_frequency('!@#!@#'), {'!': 2, '@': 2, '#': 2})
