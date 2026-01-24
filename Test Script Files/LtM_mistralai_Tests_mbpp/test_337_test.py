import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')

    def test_match_with_trailing_space(self):
        self.assertEqual(text_match_word('HelloWorld '), 'Found a match!')

    def test_match_with_leading_space(self):
        self.assertEqual(text_match_word(' HelloWorld'), 'Found a match!')

    def test_match_with_only_digits(self):
        self.assertEqual(text_match_word('1234567890'), 'Found a match!')

    def test_match_with_only_special_characters(self):
        self.assertEqual(text_match_word('!@#$%^&*()_+-=[]{}|;:,.<>?'), 'Found a match!')

    def test_match_with_only_punctuation(self):
        self.assertEqual(text_match_word('.,;:!?-'), 'Found a match!')

    def test_match_with_only_uppercase(self):
        self.assertEqual(text_match_word('HELLO'), 'Found a match!')

    def test_match_with_only_lowercase(self):
        self.assertEqual(text_match_word('helloworld'), 'Found a match!')

    def test_match_with_mixed_case(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_word('12345'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_word(''), 'Not matched!')
