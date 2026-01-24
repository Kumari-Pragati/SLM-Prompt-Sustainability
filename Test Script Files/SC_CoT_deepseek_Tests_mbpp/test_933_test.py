import unittest

from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('single'), 'single')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(camel_to_snake(' leading spaces '), '_leading_spaces_')

    def test_numbers_in_camel(self):
        self.assertEqual(camel_to_snake('camel123ToSnake'), 'camel123_to_snake')

    def test_special_characters_in_camel(self):
        self.assertEqual(camel_to_snake('camel!@#ToSnake'), 'camel!@#_to_snake')

    def test_camel_with_underscore(self):
        self.assertEqual(camel_to_snake('camel_to_snake'), 'camel_to_snake')

    def test_camel_with_mixed_case(self):
        self.assertEqual(camel_to_snake('camelMiXedCase'), 'camel_mixed_case')

    def test_camel_with_numbers_and_letters(self):
        self.assertEqual(camel_to_snake('123CamelToSnake'), '123_camel_to_snake')
