import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_Char(''), ord('a'))

    def test_single_letter(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(get_Char(char), char.upper())

    def test_multiple_letters(self):
        for string in ['aa', 'z', 'abc', 'xyz', 'abcd', 'xyzabc', 'abcdefghijklmnopqrstuvwxyz']:
            self.assertEqual(get_Char(string), chr(ord('a') + len(string) - 1))

    def test_non_alphabetic_characters(self):
        for string in ['123', '!@#$%^&*()', 'abc123', '!@#abc', 'abc!@#', 'abc!@#123']:
            self.assertEqual(get_Char(string), get_Char(string.replace(r'\W+', '')))
