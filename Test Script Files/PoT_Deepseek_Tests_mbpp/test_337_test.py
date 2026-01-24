import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_word('Hello World'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_match_word('Python'), 'Found a match!')

    def test_boundary_case_empty_string(self):
        self.assertEqual(text_match_word(''), 'Not matched!')

    def test_corner_case_whitespace_only(self):
        self.assertEqual(text_match_word('   '), 'Not matched!')

    def test_corner_case_special_characters(self):
        self.assertEqual(text_match_word('!@#$%^&*()'), 'Found a match!')

    def test_corner_case_numbers(self):
        self.assertEqual(text_match_word('1234567890'), 'Found a match!')

    def test_corner_case_mixed_case(self):
        self.assertEqual(text_match_word('PytHoN'), 'Found a match!')
