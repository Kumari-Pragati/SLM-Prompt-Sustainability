import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_word("Hello World!123"), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_word("123"), 'Not matched!')

    def test_boundary_match(self):
        self.assertEqual(text_match_word("Hello"), 'Found a match!')

    def test_boundary_no_match(self):
        self.assertEqual(text_match_word(""), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_word(None)
