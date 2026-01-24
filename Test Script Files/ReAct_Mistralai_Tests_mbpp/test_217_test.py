import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(first_Repeated_Char(char), char)

    def test_multiple_characters(self):
        for char1, char2 in [('aa', 'a'), ('ab', '\0'), ('aaa', 'a'), ('abcd', '\0'), ('aabb', 'b')]:
            self.assertEqual(first_Repeated_Char(char1), char2)

    def test_case_sensitivity(self):
        self.assertEqual(first_Repeated_Char('ABC'), '\0')
        self.assertEqual(first_Repeated_Char('aBc'), 'b')

    def test_whitespace(self):
        self.assertEqual(first_Repeated_Char(' '), ' ')
        self.assertEqual(first_Repeated_Char('  '), ' ')
        self.assertEqual(first_Repeated_Char(' abc '), ' ')

    def test_special_characters(self):
        for char in ['!@#$%^&*()_+-=[]{};:,.<>?/|\\\0123456789':
            self.assertEqual(first_Repeated_Char(char), char)

    def test_long_string(self):
        long_str = 'x' * 1000
        self.assertNotEqual(first_Repeated_Char(long_str), '\0')
