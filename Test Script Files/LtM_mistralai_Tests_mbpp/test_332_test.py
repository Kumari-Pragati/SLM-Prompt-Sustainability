import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_simple_input(self):
        self.assertDictEqual(char_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 2})

    def test_single_char_input(self):
        self.assertDictEqual(char_frequency("a"), {'a': 1})

    def test_empty_input(self):
        self.assertDictEqual(char_frequency(""), {})

    def test_case_sensitivity(self):
        self.assertDictEqual(char_frequency("HeLlo"), {'H': 1, 'e': 1, 'L': 1, 'l': 1, 'o': 2})

    def test_whitespace_input(self):
        self.assertDictEqual(char_frequency("   "), {' ': 3})

    def test_special_char_input(self):
        self.assertDictEqual(char_frequency("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"),
                             {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1,
                              '_': 1, '-': 1, '+': 1, '=': 1, '[': 1, ']': 1, '{': 1, '}': 1, '|': 1, ';': 1,
                              ':': 1, '\'': 1, '"': 1, '>': 1, '<': 1, '>': 1, '/': 1})
