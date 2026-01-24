import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(char_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 2})
        self.assertDictEqual(char_frequency("Python"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1})

    def test_edge_case_empty_string(self):
        self.assertDictEqual(char_frequency(""), {})

    def test_edge_case_single_character(self):
        self.assertDictEqual(char_frequency("a"), {'a': 1})

    def test_edge_case_whitespace(self):
        self.assertDictEqual(char_frequency(" "), {' ': 1})

    def test_edge_case_special_characters(self):
        self.assertDictEqual(char_frequency("!@#$%^&*()_+-="),
                             {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1,
                              '_': 1, '+': 1, '-': 1, '=': 1})

    def test_corner_case_unicode(self):
        self.assertDictEqual(char_frequency("\u00E9"), {'\u00E9': 1})
