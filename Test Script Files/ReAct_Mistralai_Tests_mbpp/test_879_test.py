import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match_with_a_and_b(self):
        """Test if the function correctly identifies a match with 'a' and 'b'."""
        self.assertEqual(text_match('aaab'), 'Found a match!')

    def test_match_with_only_a(self):
        """Test if the function correctly identifies no match with only 'a'."""
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_match_with_only_b(self):
        """Test if the function correctly identifies no match with only 'b'."""
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_match_with_a_and_b_in_different_order(self):
        """Test if the function correctly identifies a match with 'a' and 'b' in different order."""
        self.assertEqual(text_match('bbaa'), 'Found a match!')

    def test_match_with_multiple_a_and_b(self):
        """Test if the function correctly identifies a match with multiple 'a' and 'b'."""
        self.assertEqual(text_match('aaaaabbbb'), 'Found a match!')

    def test_match_with_leading_and_trailing_spaces(self):
        """Test if the function correctly identifies a match with leading and trailing spaces."""
        self.assertEqual(text_match('   aaab   '), 'Found a match!')

    def test_match_with_empty_string(self):
        """Test if the function correctly identifies no match with an empty string."""
        self.assertEqual(text_match(''), 'Not matched!')

    def test_match_with_only_dot(self):
        """Test if the function correctly identifies no match with only '.'."""
        self.assertEqual(text_match('.'), 'Not matched!')
