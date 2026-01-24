import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_empty_string(self):
        """Test that an empty string returns 0"""
        self.assertEqual(string_length(''), 0)

    def test_single_character_string(self):
        """Test that a single character string returns 1"""
        self.assertEqual(string_length('a'), 1)

    def test_multiple_characters_string(self):
        """Test that a multi-character string returns the correct length"""
        self.assertEqual(string_length('abc'), 3)

    def test_long_string(self):
        """Test that a long string returns the correct length"""
        self.assertEqual(string_length('xyz1234567890'), 19)

    def test_string_with_spaces(self):
        """Test that a string with spaces returns the correct length"""
        self.assertEqual(string_length('Hello World'), 11)

    def test_unicode_string(self):
        """Test that a unicode string returns the correct length"""
        self.assertEqual(string_length('\u4e2d\u6587'), 2)

    def test_string_with_special_characters(self):
        """Test that a string with special characters returns the correct length"""
        self.assertEqual(string_length('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 47)

    def test_string_with_only_special_characters(self):
        """Test that a string with only special characters returns the correct length"""
        self.assertEqual(string_length('!@#$%^&*()_+-=[]{}|;:'\'<>,.'), 38)

    def test_string_with_empty_spaces(self):
        """Test that a string with empty spaces returns the correct length"""
        self.assertEqual(string_length('  \t\n\r   '), 5)

    def test_string_with_only_whitespace(self):
        """Test that a string with only whitespace returns the correct length"""
        self.assertEqual(string_length('\t\n\r '), 4)
