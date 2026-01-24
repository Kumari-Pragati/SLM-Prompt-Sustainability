import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_empty_string(self):
        """Test max_char on an empty string"""
        self.assertEqual(max_char(''), '')

    def test_single_character_string(self):
        """Test max_char on a string with a single character"""
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(max_char(char), char)

    def test_multiple_characters_string(self):
        """Test max_char on a string with multiple characters"""
        for char1, char2 in [('aa', 'a'), ('ab', 'a'), ('ba', 'b'), ('bb', 'b')]:
            self.assertEqual(max_char(char1), char2)

    def test_case_insensitive(self):
        """Test max_char is case-insensitive"""
        for char1, char2 in [('Aa', 'a'), ('Ab', 'a'), ('BA', 'b'), ('BB', 'b')]:
            self.assertEqual(max_char(char1), char2)

    def test_multiple_occurrences(self):
        """Test max_char handles multiple occurrences correctly"""
        for string in ['aaa', 'aaab', 'aaaaa', 'aaaab', 'aaaaaaa']:
            self.assertEqual(max_char(string), 'a')

    def test_string_with_spaces(self):
        """Test max_char on a string with spaces"""
        self.assertEqual(max_char('Hello, World!'), ' ')

    def test_string_with_special_characters(self):
        """Test max_char on a string with special characters"""
        for string in ['!@#$%^&*()_+-=', 'Hello, World!12345', 'Hello, World!@#$%^&*()_+-=']:
            self.assertEqual(max_char(string), string[0])

    def test_string_with_numbers(self):
        """Test max_char on a string with numbers"""
        for string in ['12345', '123456', '1234567', '12345678', '123456789']:
            self.assertEqual(max_char(string), '1')
