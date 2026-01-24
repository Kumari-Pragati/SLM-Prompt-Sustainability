import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('ThisIsCamelCase'), 'this_is_camel_case')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_numbers(self):
        self.assertEqual(camel_to_snake('3CamelCase'), '3_camel_case')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('Camel$Case'), 'camel_$case')

    def test_spaces(self):
        self.assertEqual(camel_to_snake('Camel Case'), 'camel_case')

    def test_invalid_input(self):
        self.assertRaises(TypeError, camel_to_snake, 123)
