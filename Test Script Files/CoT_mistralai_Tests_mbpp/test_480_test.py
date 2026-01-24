import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_single_character(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_multiple_characters(self):
        self.assertEqual(get_max_occuring_char('abracadabra'), 'a')

    def test_case_sensitivity(self):
        self.assertEqual(get_max_occuring_char('ABC'), 'C')

    def test_whitespace(self):
        self.assertEqual(get_max_occuring_char('   '), ' ')

    def test_special_characters(self):
        self.assertEqual(get_max_occuring_char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '!')

    def test_unicode_characters(self):
        self.assertEqual(get_max_occuring_char('\u00E9'), '\u00E9')

    def test_multiple_max_occurring_char(self):
        self.assertEqual(get_max_occuring_char('aaabbc'), 'a')

    def test_minimum_input_length(self):
        self.assertEqual(get_max_occuring_char(chr(0)), chr(0))
