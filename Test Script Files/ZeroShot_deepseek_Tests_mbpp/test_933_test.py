import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('camelCaseAndAnotherCase'), 'camel_case_and_another_case')

    def test_numbers_in_word(self):
        self.assertEqual(camel_to_snake('camelCaseWith123'), 'camel_case_with123')

    def test_all_uppercase(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'all_caps')

    def test_all_lowercase(self):
        self.assertEqual(camel_to_snake('alllowercase'), 'alllowercase')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MiXeDcAsE'), 'mixed_case')
