import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')

    def test_edge_case_with_whitespace(self):
        self.assertEqual(text_match_word('Hello World'), 'Found a match!')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(text_match_word('Hello@World'), 'Found a match!')

    def test_edge_case_with_numbers(self):
        self.assertEqual(text_match_word('Hello123World'), 'Found a match!')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(text_match_word(''), 'Not matched!')

    def test_edge_case_with_none(self):
        with self.assertRaises(TypeError):
            text_match_word(None)
