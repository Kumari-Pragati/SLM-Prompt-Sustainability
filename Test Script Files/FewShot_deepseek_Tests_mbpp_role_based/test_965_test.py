import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('snake'), 'snake')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MiXeDcAsE'), 'mixed_case')

    def test_numbers_in_camel(self):
        self.assertEqual(camel_to_snake('camel1To2Snake'), 'camel1_to2_snake')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_whitespace_in_camel(self):
        self.assertEqual(camel_to_snake('camel To Snake'), 'camel_to_snake')

    def test_special_characters_in_camel(self):
        self.assertEqual(camel_to_snake('camel@To#Snake'), 'camel@to#snake')
