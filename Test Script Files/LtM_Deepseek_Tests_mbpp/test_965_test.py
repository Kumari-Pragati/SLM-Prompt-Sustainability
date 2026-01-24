import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_simple_camel_to_snake(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_camel_with_numbers_to_snake(self):
        self.assertEqual(camel_to_snake('camel1ToSnake2'), 'camel1_to_snake2')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_word_camel_to_snake(self):
        self.assertEqual(camel_to_snake('singleWord'), 'single_word')

    def test_camel_with_special_chars_to_snake(self):
        self.assertEqual(camel_to_snake('camel$ToSnake@'), 'camel_to_snake')

    def test_camel_with_mixed_case_to_snake(self):
        self.assertEqual(camel_to_snake('camelMiXeD'), 'camel_mixed')

    def test_camel_with_leading_number_to_snake(self):
        self.assertEqual(camel_to_snake('123CamelToSnake'), '123_camel_to_snake')

    def test_camel_with_trailing_number_to_snake(self):
        self.assertEqual(camel_to_snake('CamelToSnake456'), 'camel_to_snake456')

    def test_camel_with_mixed_case_and_numbers_to_snake(self):
        self.assertEqual(camel_to_snake('CaMeL1MiXeD2'), 'camel1_mixed2')
