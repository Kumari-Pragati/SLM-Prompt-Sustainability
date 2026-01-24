import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_found_with_three_chars(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_match_found_with_two_chars(self):
        self.assertEqual(text_match_two_three('aba'), 'Found a match!')

    def test_match_found_with_three_chars_and_space(self):
        self.assertEqual(text_match_two_three('ab abab'), 'Found a match!')

    def test_match_found_with_three_chars_and_newline(self):
        self.assertEqual(text_match_two_three('ab\nabab'), 'Found a match!')

    def test_match_found_with_three_chars_and_tab(self):
        self.assertEqual(text_match_two_three('ab\tabab'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces(self):
        self.assertEqual(text_match_two_three('ab   abab'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_newlines(self):
        self.assertEqual(text_match_two_three('ab\n\nabab\n'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_tabs(self):
        self.assertEqual(text_match_two_three('ab\t\tabab\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines(self):
        self.assertEqual(text_match_two_three('ab   \n\tabab\n'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_tabs(self):
        self.assertEqual(text_match_two_three('ab   \t\tabab\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   '), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t\n'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t\n\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t\n\t   \t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t\n\t   \t\n'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs(self):
        self.assertEqual(text_match_two_three('ab   \n\t\tabab\n\t   \n\t   \t\n\t   \t\n\t'), 'Found a match!')

    def test_match_found_with_three_chars_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and_newlines_and_tabs_and_multiple_spaces_and