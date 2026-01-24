import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('camelCaseAnotherExample'), 'camel_case_another_example')

    def test_numbers_in_word(self):
        self.assertEqual(camel_to_snake('camelCase123Example'), 'camel_case123_example')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'all_caps')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MiXeDcAsE'), 'mixed_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')
