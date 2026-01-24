import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_single_word_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words_camel_case(self):
        self.assertEqual(camel_to_snake('MultiWordCamelCase'), 'multi_word_camel_case')

    def test_already_snake_case(self):
        self.assertEqual(camel_to_snake('already_snake_case'), 'already_snake_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(camel_to_snake('camel123Case'), 'camel123_case')

    def test_string_with_special_characters(self):
        self.assertEqual(camel_to_snake('camel!@#Case'), 'camel!@#_case')

    def test_string_with_mixed_case(self):
        self.assertEqual(camel_to_snake('camelMiXeDcAsE'), 'camel_mixed_case')

    def test_string_with_capital_letter_at_start(self):
        self.assertEqual(camel_to_snake('CamelMiXeDcAsE'), 'camel_mixed_case')

    def test_string_with_capital_letter_at_end(self):
        self.assertEqual(camel_to_snake('camelMiXeDcAsEe'), 'camel_mixed_casee')

    def test_string_with_capital_letter_only(self):
        self.assertEqual(camel_to_snake('CAPSLOCK'), 'capslock')

    def test_string_with_all_lowercase(self):
        self.assertEqual(camel_to_snake('alllowercase'), 'alllowercase')

    def test_string_with_all_uppercase(self):
        self.assertEqual(camel_to_snake('ALLUPPERCASE'), 'alluppercase')
