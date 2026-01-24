import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_empty_string(self):
        """Checks that an empty string returns None"""
        self.assertIsNone(ascii_value_string(''))

    def test_single_char_string(self):
        """Checks that a single character string returns the correct ASCII value"""
        for char, expected in [('a', 97), ('A', 65), ('0', 48), ('!', 33)]:
            self.assertEqual(ascii_value_string(char), expected)

    def test_multi_char_string(self):
        """Checks that a multi-character string returns a list of ASCII values"""
        for string, expected in [('abc', [97, 98, 99]), ('ABC', [65, 66, 67]), ('012', [48, 49, 50])]:
            self.assertEqual(ascii_value_string(string), expected)

    def test_string_with_non_ascii(self):
        """Checks that non-ASCII characters raise a ValueError"""
        self.assertRaises(ValueError, ascii_value_string, 'é')
