import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match_word("HelloWorld"), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_word(""), 'Not matched!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_match_word("word"), 'Found a match!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_match_word("a"), 'Not matched!')

    def test_edge_case_only_digits(self):
        self.assertEqual(text_match_word("12345"), 'Not matched!')

    def test_edge_case_only_special_characters(self):
        self.assertEqual(text_match_word("!@#$%^&*()"), 'Not matched!')

    def test_edge_case_only_punctuation(self):
        self.assertEqual(text_match_word(".,;:!?"), 'Not matched!')

    def test_edge_case_only_whitespace(self):
        self.assertEqual(text_match_word("   "), 'Not matched!')

    def test_edge_case_leading_whitespace(self):
        self.assertEqual(text_match_word("   HelloWorld"), 'Found a match!')

    def test_edge_case_trailing_whitespace(self):
        self.assertEqual(text_match_word("HelloWorld   "), 'Found a match!')
