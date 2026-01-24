import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_lowercase_underscore(self):
        self.assertEqual(text_lowercase_underscore('low_ercase'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('UPPER_CASE'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_Uppercase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_uppercase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_Uppercase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_uppercase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_Uppercase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('lowercase_uppercase'), 'Not matched!')
