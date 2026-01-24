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

    def test_whitespace_string(self):
        self.assertEqual(get_max_occuring_char('   '), ' ')

    def test_special_characters(self):
        self.assertEqual(get_max_occuring_char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '!')

    def test_unicode_string(self):
        self.assertEqual(get_max_occuring_char('\u00E9l\u00E9ph\u00E9r'), '\u00E9')

    def test_max_ascii_value(self):
        self.assertEqual(get_max_occuring_char(chr(255)), chr(255))

    def test_min_ascii_value(self):
        self.assertEqual(get_max_occuring_char(chr(0)), chr(0))

    def test_single_max_occurrence(self):
        self.assertEqual(get_max_occuring_char('aaabbc'), 'a')

    def test_multiple_max_occurrences(self):
        self.assertEqual(get_max_occuring_char('aaabbcbb'), 'b')

    def test_no_max_occurrences(self):
        self.assertEqual(get_max_occuring_char('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'), '')
