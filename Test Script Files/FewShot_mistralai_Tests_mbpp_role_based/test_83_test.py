import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_Char(''), ord('a'))

    def test_single_letter(self):
        self.assertEqual(get_Char('a'), ord('b'))
        self.assertEqual(get_Char('z'), ord('a'))

    def test_multiple_letters(self):
        self.assertEqual(get_Char('abc'), ord('d'))
        self.assertEqual(get_Char('zyx'), ord('aa'))

    def test_string_with_numbers(self):
        self.assertEqual(get_Char('abc123'), ord('d'))
        self.assertEqual(get_Char('123abc'), ord('d'))

    def test_string_with_special_characters(self):
        self.assertEqual(get_Char('abc!@#'), ord('d'))
        self.assertEqual(get_Char('!@#abc'), ord('d'))

    def test_string_with_punctuation(self):
        self.assertEqual(get_Char('abc.,'), ord('d'))
        self.assertEqual(get_Char(',abc.'), ord('d'))

    def test_string_with_whitespace(self):
        self.assertEqual(get_Char('abc '), ord('d'))
        self.assertEqual(get_Char(' abc'), ord('d'))
