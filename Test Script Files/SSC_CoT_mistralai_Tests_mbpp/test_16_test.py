import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(text_lowercase_underscore('example_name'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('another_example'), 'Found a match!')

    def test_edge_input(self):
        self.assertNotEqual(text_lowercase_underscore('example'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('_example'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('Example_'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_123'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('123_example'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_Example'), 'Found a match!')

    def test_special_input(self):
        self.assertNotEqual(text_lowercase_underscore('example_123_456'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_123_456_789'), 'Found a match!')
        self.assertNotEqual(text_lowercase_underscore('example_123_456_789_0'), 'Found a match!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, text_lowercase_underscore, 123)
        self.assertRaises(TypeError, text_lowercase_underscore, [1, 2, 3])
        self.assertRaises(TypeError, text_lowercase_underscore, (1, 2, 3))
        self.assertRaises(TypeError, text_lowercase_underscore, {'key': 'value'})
        self.assertRaises(TypeError, text_lowercase_underscore, None)
