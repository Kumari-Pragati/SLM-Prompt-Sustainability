import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_match(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_word(""), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_word(None)
