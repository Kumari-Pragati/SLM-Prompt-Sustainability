import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_case(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')

    def test_mixed_case(self):
        self.assertEqual(text_uppercase_lowercase('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('AbCdEfGhIjKlMnOpQrStUvWxYz123'), 'Not matched!')

    def test_all_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'Found a match!')

    def test_all_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('abcdefghijklmnopqrstuvwxyz'), 'Not matched!')

    def test_long_string(self):
        long_string = 'A' * 100 + 'a' * 100 + '$'
        self.assertEqual(text_uppercase_lowercase(long_string), 'Found a match!')
