import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_match_three_characters(self):
        """Test if the function correctly identifies a match with exactly three 'a's or 'b's."""
        self.assertEqual(text_match_three('aaa'), 'Found a match!')
        self.assertEqual(text_match_three('bbb'), 'Found a match!')

    def test_match_three_characters_with_spaces(self):
        """Test if the function correctly identifies a match with exactly three 'a's or 'b's, even with spaces."""
        self.assertEqual(text_match_three(' aaa '), 'Found a match!')
        self.assertEqual(text_match_three(' bbb '), 'Found a match!')

    def test_match_three_characters_in_mixed_string(self):
        """Test if the function correctly identifies a match with exactly three 'a's or 'b's, even in a mixed string."""
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_match_less_than_three_characters(self):
        """Test if the function correctly identifies no match when less than three 'a's or 'b's are present."""
        self.assertEqual(text_match_three('aa'), 'Not matched!')
        self.assertEqual(text_match_three('ab'), 'Not matched!')
        self.assertEqual(text_match_three('a'), 'Not matched!')
        self.assertEqual(text_match_three('b'), 'Not matched!')

    def test_match_more_than_three_characters(self):
        """Test if the function correctly identifies no match when more than three 'a's or 'b's are present."""
        self.assertEqual(text_match_three('aaaaa'), 'Not matched!')
        self.assertEqual(text_match_three('bbbbb'), 'Not matched!')

    def test_match_three_with_special_characters(self):
        """Test if the function correctly identifies a match with exactly three 'a's or 'b's, even with special characters."""
        self.assertEqual(text_match_three('ab!@#$%^&*()_'), 'Not matched!')
        self.assertEqual(text_match_three('!@#$%^&*()_aaa'), 'Not matched!')
        self.assertEqual(text_match_three('!@#$%^&*()_bbb'), 'Not matched!')
        self.assertEqual(text_match_three('aaa!@#$%^&*()_'), 'Found a match!')
        self.assertEqual(text_match_three('bbb!@#$%^&*()_'), 'Found a match!')
