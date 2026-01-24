import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_word("HelloWorld"), 'Found a match!')
        self.assertEqual(text_match_word("123456789"), 'Found a match!')
        self.assertEqual(text_match_word("_abcdefg"), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_word(""), 'Not matched!')
        self.assertEqual(text_match_word(" "), 'Not matched!')
        self.assertEqual(text_match_word("Hello"), 'Not matched!')
        self.assertEqual(text_match_word("World!"), 'Not matched!')
        self.assertEqual(text_match_word("1234567890"), 'Not matched!')
        self.assertEqual(text_match_word("_"), 'Not matched!')

    def test_corner_case(self):
        self.assertEqual(text_match_word("HelloWorld!"), 'Found a match!')
        self.assertEqual(text_match_word("_abcdefg_"), 'Found a match!')
        self.assertEqual(text_match_word("12345678901"), 'Not matched!')
        self.assertEqual(text_match_word("__"), 'Not matched!')
