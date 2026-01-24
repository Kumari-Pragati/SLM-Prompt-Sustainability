import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_single_char(self):
        self.assertEqual(first_Repeated_Char('a'), 'a')
        self.assertEqual(first_Repeated_Char('b'), '\0')
        self.assertEqual(first_Repeated_Char('c'), 'c')

    def test_multiple_chars(self):
        self.assertEqual(first_Repeated_Char('aa'), 'a')
        self.assertEqual(first_Repeated_Char('ab'), '\0')
        self.assertEqual(first_Repeated_Char('abc'), '\0')
        self.assertEqual(first_Repeated_Char('aab'), 'a')
        self.assertEqual(first_Repeated_Char('abcba'), 'b')

    def test_special_characters(self):
        self.assertEqual(first_Repeated_Char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '\0')
        self.assertEqual(first_Repeated_Char('!@#a$%^&*()_+-=[]{}|;:,.<>?'), 'a')
        self.assertEqual(first_Repeated_Char('a!@#$%^&*()_+-=[]{}|;:,.<>?'), '\0')
