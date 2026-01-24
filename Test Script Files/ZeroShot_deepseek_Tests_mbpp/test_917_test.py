import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_uppercase_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('AbcDe'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('abcde'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('ABC'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('AbCdEfGh'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('abcdefgh'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('ABCDEFGH'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('AbC'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('ABCDEF'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('abcdefghijklmnopqrstuvwxyz'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'Not matched!')
