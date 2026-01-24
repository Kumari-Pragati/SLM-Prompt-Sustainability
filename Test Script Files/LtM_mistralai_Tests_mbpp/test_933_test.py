import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('Valid_Identifier'), 'valid_identifier')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('1A'), '1_a')
        self.assertEqual(camel_to_snake('A1'), 'a_1')
        self.assertEqual(camel_to_snake('A_1'), 'a_1')
        self.assertEqual(camel_to_snake('__'), '__')
        self.assertEqual(camel_to_snake('__A'), '_a')
        self.assertEqual(camel_to_snake('A__'), 'a_')

    def test_complex_cases(self):
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumbers'), 'valid_identifier_with_numbers')
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumbersAndUnderscores'), 'valid_identifier_with_numbers_and_underscores')
        self.assertEqual(camel_to_snake('ValidIdentifierWithNumbersAndMixedCases'), 'valid_identifier_with_numbers_and_mixed_cases')
