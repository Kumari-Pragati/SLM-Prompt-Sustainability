import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_empty_string(self):
        """Test if an empty string returns expected character"""
        self.assertEqual(get_Char(""), ord('a'))

    def test_single_letter(self):
        """Test if a single letter returns expected character"""
        for char in range(ord('a'), ord('z')+1):
            self.assertEqual(get_Char(chr(char)), chr(char+1))

    def test_long_string(self):
        """Test if a long string returns expected character"""
        test_string = 'abcdefghijklmnopqrstuvwxyz' * 5
        expected_char = chr((ord('z') + 5) % 26 + ord('a'))
        self.assertEqual(get_Char(test_string), expected_char)

    def test_string_with_numbers(self):
        """Test if a string with numbers is handled correctly"""
        test_string = 'abc123def'
        self.assertEqual(get_Char(test_string), get_Char('cdef'))

    def test_string_with_special_characters(self):
        """Test if a string with special characters is handled correctly"""
        test_string = 'abc!@#$%def'
        self.assertEqual(get_Char(test_string), get_Char('cdef'))

    def test_string_with_uppercase_letters(self):
        """Test if a string with uppercase letters is handled correctly"""
        test_string = 'ABCabc'
        self.assertEqual(get_Char(test_string), get_Char('cabc'))

    def test_string_with_repeated_letters(self):
        """Test if a string with repeated letters is handled correctly"""
        test_string = 'aaaaaa'
        self.assertEqual(get_Char(test_string), get_Char('aaa'))
