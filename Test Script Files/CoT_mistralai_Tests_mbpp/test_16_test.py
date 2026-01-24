import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(text_lowercase_underscore('valid_input'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('Valid_Input'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('valid_input_123'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('Valid_Input_123'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('a'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('__'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('___'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('____'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('_____'), 'Not matched!')

    def test_invalid_inputs(self):
        self.assertEqual(text_lowercase_underscore(123), 'Not matched!')
        self.assertEqual(text_lowercase_underscore(None), 'Not matched!')
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')
        self.assertEqual(text_lowercase_underscore(' '), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('_'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('__'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('___'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('____'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('_____'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('UpperCase'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('UpperCase_'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('UpperCase_Lower'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('UpperCase_Lower_'), 'Not matched!')
