import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_match_word(self):
        self.assertEqual(text_match_word("Hello World"), 'Found a match!')

    def test_no_match_word(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_match_word_at_end(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_no_match_word_at_end(self):
        self.assertEqual(text_match_word("Hello!"), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_word(""), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_word(123)
