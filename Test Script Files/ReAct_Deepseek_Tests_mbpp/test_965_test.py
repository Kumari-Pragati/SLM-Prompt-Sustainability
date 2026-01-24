import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('single'), 'single')

    def test_already_snake_case(self):
        self.assertEqual(camel_to_snake('already_in_snake_case'), 'already_in_snake_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_number_in_word(self):
        self.assertEqual(camel_to_snake('number2Word'), 'number2_word')

    def test_number_as_first_char(self):
        self.assertEqual(camel_to_snake('123Start'), '123_start')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('special@chars'), 'special_chars')

    def test_special_characters_in_word(self):
        self.assertEqual(camel_to_snake('wordWith$pecialCh@rs'), 'word_with_special_ch_rs')
