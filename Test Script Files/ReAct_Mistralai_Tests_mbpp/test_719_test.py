import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_empty_string(self):
        """Test if an empty string returns 'Not matched!'"""
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        """Test if 'a' returns 'Not matched!'"""
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_multiple_a(self):
        """Test if 'aa' returns 'Found a match!'"""
        self.assertEqual(text_match('aa'), 'Found a match!')

    def test_multiple_ab(self):
        """Test if 'ab' returns 'Found a match!'"""
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_multiple_ab_with_space(self):
        """Test if 'ab ' returns 'Found a match!'"""
        self.assertEqual(text_match('ab '), 'Found a match!')

    def test_multiple_ab_with_newline(self):
        """Test if 'ab\n' returns 'Found a match!'"""
        self.assertEqual(text_match('ab\n'), 'Found a match!')

    def test_multiple_ab_with_multiple_spaces(self):
        """Test if 'ab   ' returns 'Found a match!'"""
        self.assertEqual(text_match('ab   '), 'Found a match!')

    def test_multiple_ab_with_multiple_newlines(self):
        """Test if 'ab\n\n' returns 'Found a match!'"""
        self.assertEqual(text_match('ab\n\n'), 'Found a match!')

    def test_multiple_ab_with_other_characters(self):
        """Test if 'abc' returns 'Not matched!'"""
        self.assertEqual(text_match('abc'), 'Not matched!')
