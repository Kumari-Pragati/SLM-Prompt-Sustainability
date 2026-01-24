import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(first_Repeated_Char('a'), 'a')

    def test_no_repeated_chars(self):
        self.assertEqual(first_Repeated_Char('abc'), '\0')

    def test_repeated_chars(self):
        self.assertEqual(first_Repeated_Char('aabbcc'), 'a')

    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_single_char_string(self):
        self.assertEqual(first_Repeated_Char('a'), 'a')

    def test_repeated_chars_at_start(self):
        self.assertEqual(first_Repeated_Char('aaabbb'), 'a')

    def test_repeated_chars_at_end(self):
        self.assertEqual(first_Repeated_Char('abcba'), 'a')

    def test_repeated_chars_in_middle(self):
        self.assertEqual(first_Repeated_Char('abacba'), 'a')
