import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('ValidNumber'), 'valid_number')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('A'), '_a')
        self.assertEqual(camel_to_snake('a'), '_a')
        self.assertEqual(camel_to_snake('Aa'), '_aa')
        self.assertEqual(camel_to_snake('1'), '_1')
        self.assertEqual(camel_to_snake('1A'), '_1_a')
        self.assertEqual(camel_to_snake('A1'), '_a_1')

    def test_complex_cases(self):
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumber'), 'valid_identifier_with_number')
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumberAndSpecialChar'), 'valid_identifier_with_number_and_special_char')
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumberAndSpecialCharAtBeginning'), '_valid_identifier_with_number_and_special_char')
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumberAtBeginning'), '_valid_identifier_with_number')
