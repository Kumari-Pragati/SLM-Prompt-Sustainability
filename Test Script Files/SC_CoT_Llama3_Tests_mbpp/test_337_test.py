import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_edge_case_starting_with_word(self):
        self.assertEqual(text_match_word("Word!"), 'Found a match!')

    def test_edge_case_starting_with_non_word(self):
        self.assertEqual(text_match_word("123"), 'Not matched!')

    def test_edge_case_end_with_word(self):
        self.assertEqual(text_match_word("World!"), 'Found a match!')

    def test_edge_case_end_with_non_word(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_edge_case_start_and_end_with_word(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_edge_case_start_and_end_with_non_word(self):
        self.assertEqual(text_match_word("123456"), 'Not matched!')

    def test_edge_case_start_with_word_and_end_with_non_word(self):
        self.assertEqual(text_match_word("Hello 123"), 'Not matched!')

    def test_edge_case_start_with_non_word_and_end_with_word(self):
        self.assertEqual(text_match_word("123 World!"), 'Not matched!')

    def test_edge_case_start_with_word_and_end_with_word(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_edge_case_start_with_non_word_and_end_with_non_word(self):
        self.assertEqual(text_match_word("123456"), 'Not matched!')
