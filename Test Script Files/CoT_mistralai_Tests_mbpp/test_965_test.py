import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('PascalCase'), 'pascal_case')
        self.assertEqual(camel_to_snake('FirstSecond'), 'first_second')
        self.assertEqual(camel_to_snake('First2nd'), 'first_2nd')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('mixedCase'), 'mixed_case')
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_numbers(self):
        self.assertEqual(camel_to_snake('123CamelCase'), '123_camel_case')
        self.assertEqual(camel_to_snake('Camel123Case'), 'camel_123_case')
        self.assertEqual(camel_to_snake('1_2_3CamelCase'), '1_2_3_camel_case')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('CamelWithSpecial_Case'), 'camel_with_special__case')
        self.assertEqual(camel_to_snake('CamelWithSpecialCase'), 'camel_with_special_case')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('Aa'), 'aa')
        self.assertEqual(camel_to_snake('A_'), 'a_')
        self.assertEqual(camel_to_snake('__'), '__')
        self.assertEqual(camel_to_snake('A__'), 'a__')
        self.assertEqual(camel_to_snake('A__A'), 'a__a')
