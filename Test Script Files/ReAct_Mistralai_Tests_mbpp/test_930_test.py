import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_empty_string(self):
        """Test if empty string returns 'Not matched!'"""
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        """Test if 'a' returns 'Found a match!'"""
        self.assertEqual(text_match('a'), 'Found a match!')

    def test_multiple_a(self):
        """Test if 'aa' returns 'Found a match!'"""
        self.assertEqual(text_match('aa'), 'Found a match!')

    def test_multiple_ab(self):
        """Test if 'ab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_multiple_abab(self):
        """Test if 'abab' returns 'Found a match!'"""
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_multiple_abab_with_space(self):
        """Test if 'ab ab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab ab'), 'Found a match!')

    def test_multiple_abab_with_newline(self):
        """Test if 'ab\nab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab\nab'), 'Found a match!')

    def test_multiple_abab_with_multiple_spaces(self):
        """Test if 'ab   ab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab   ab'), 'Found a match!')

    def test_multiple_abab_with_multiple_newlines(self):
        """Test if 'ab\n\nab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab\n\nab'), 'Found a match!')

    def test_multiple_abab_with_special_characters(self):
        """Test if 'ab!ab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab!ab'), 'Found a match!')

    def test_multiple_abab_with_numbers(self):
        """Test if 'ab1ab' returns 'Not matched!'"""
        self.assertEqual(text_match('ab1ab'), 'Not matched!')
