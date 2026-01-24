import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_single_character(self):
        self.assertEqual(first_Repeated_Char('a'), 'a')

    def test_multiple_characters_no_repeats(self):
        self.assertEqual(first_Repeated_Char('abcdefg'), '\0')

    def test_multiple_characters_with_repeats(self):
        self.assertEqual(first_Repeated_Char('aaabbc'), 'a')

    def test_case_sensitivity(self):
        self.assertEqual(first_Repeated_Char('ABC'), '\0')
        self.assertEqual(first_Repeated_Char('aBc'), '\0')
        self.assertEqual(first_Repeated_Char('AbC'), '\0')

    def test_whitespace(self):
        self.assertEqual(first_Repeated_Char(' \t\n\r '), '\0')

    def test_special_characters(self):
        self.assertEqual(first_Repeated_Char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '\0')

    def test_unicode(self):
        self.assertEqual(first_Repeated_Char('\u00E9'), '\u00E9')
