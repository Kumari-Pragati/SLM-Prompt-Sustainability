import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')

    def test_edge_condition_empty_string(self):
        self.assertEqual(text_match_word(''), 'Not matched!')

    def test_boundary_condition_single_word(self):
        self.assertEqual(text_match_word('SingleWord'), 'Found a match!')

    def test_boundary_condition_multiple_words(self):
        self.assertEqual(text_match_word('Multiple Words'), 'Not matched!')

    def test_complex_condition_special_characters(self):
        self.assertEqual(text_match_word('Special@Characters'), 'Found a match!')

    def test_complex_condition_numbers(self):
        self.assertEqual(text_match_word('Numbers123'), 'Found a match!')
