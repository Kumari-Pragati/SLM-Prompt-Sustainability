import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_empty_string(self):
        """Test counting characters in an empty string"""
        self.assertEqual(count_charac(''), 0)

    def test_single_character(self):
        """Test counting characters in a single character string"""
        self.assertEqual(count_charac('a'), 1)

    def test_multiple_characters(self):
        """Test counting characters in a multi-character string"""
        self.assertEqual(count_charac('abc'), 3)

    def test_whitespace(self):
        """Test counting characters in a string with whitespace"""
        self.assertEqual(count_charac(' a b c '), 5)

    def test_long_string(self):
        """Test counting characters in a long string"""
        long_string = 'x' * 100
        self.assertEqual(len(long_string), count_charac(long_string))

    def test_unicode_string(self):
        """Test counting characters in a unicode string"""
        self.assertEqual(count_charac('\u00A9'), 1)

    def test_string_with_non_printable_characters(self):
        """Test counting characters in a string with non-printable characters"""
        self.assertEqual(count_charac('\x00'), 1)
