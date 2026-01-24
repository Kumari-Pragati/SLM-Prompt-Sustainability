import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_repeated_char_in_string(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')
        self.assertEqual(first_Repeated_Char('abcdef'), '\0')
        self.assertEqual(first_Repeated_Char('aabbcc'), 'a')
        self.assertEqual(first_Repeated_Char('123123'), '1')
        self.assertEqual(first_Repeated_Char('abc'), '\0')

    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_string_with_special_characters(self):
        self.assertEqual(first_Repeated_Char('!@#!@#'), '!')
        self.assertEqual(first_Repeated_Char('abcde$%^&*abc'), 'a')

    def test_string_with_numbers_and_special_characters(self):
        self.assertEqual(first_Repeated_Char('12345678901234567890'), '1')
        self.assertEqual(first_Repeated_Char('!@#$%^&*()1234567890'), '1')
