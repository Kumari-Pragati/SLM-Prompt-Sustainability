import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_lowercase_underscore_with_valid_input(self):
        """Test if the function correctly identifies valid input"""
        self.assertEqual(text_lowercase_underscore('example_variable'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('another_example'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('long_string_with_underscores'), 'Found a match!')

    def test_lowercase_underscore_with_invalid_input(self):
        """Test if the function correctly identifies invalid input"""
        self.assertNotEqual(text_lowercase_underscore('Example_Variable'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_123'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_variable_'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore(''), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('123'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('_example'), 'Found a match!')
