import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(char_frequency('hello'), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_empty_string(self):
        self.assertEqual(char_frequency(''), {})

    def test_single_character(self):
        self.assertEqual(char_frequency('a'), {'a': 1})

    def test_case_sensitivity(self):
        self.assertNotEqual(char_frequency('Hello'), char_frequency('hello'))

    def test_special_characters(self):
        self.assertEqual(char_frequency('!@#$%^&*()'), {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1})

    def test_numeric_characters(self):
        self.assertEqual(char_frequency('1234567890'), {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1})

    def test_whitespace(self):
        self.assertEqual(char_frequency(' '), {' ': 1})

    def test_multiple_spaces(self):
        self.assertEqual(char_frequency('   '), {' ': 3})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            char_frequency(12345)
