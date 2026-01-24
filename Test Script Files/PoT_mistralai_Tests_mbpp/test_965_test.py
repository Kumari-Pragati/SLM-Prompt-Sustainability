import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('Valid_Identifier'), 'valid_identifier')

    def test_edge_case_uppercase_first_letter(self):
        self.assertEqual(camel_to_snake('UpperCase'), 'upper_case')

    def test_edge_case_uppercase_middle_letter(self):
        self.assertEqual(camel_to_snake('MiddleCase'), 'middle_case')

    def test_edge_case_uppercase_last_letter(self):
        self.assertEqual(camel_to_snake('LastCase'), 'last_case')

    def test_edge_case_mixed_case(self):
        self.assertEqual(camel_to_snake('mixedCase'), 'mixed_case')

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_edge_case_single_letter(self):
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('B'), 'b')
        self.assertEqual(camel_to_snake('Z'), 'z')

    def test_edge_case_numbers(self):
        self.assertEqual(camel_to_snake('123CamelCase'), '123_camel_case')
        self.assertEqual(camel_to_snake('CamelCase123'), 'camel_case_123')
        self.assertEqual(camel_to_snake('123'), '123')

    def test_edge_case_special_characters(self):
        self.assertEqual(camel_to_snake('Camel$Case'), 'camel_$case')
        self.assertEqual(camel_to_snake('Camel_Case'), 'camel_case')
        self.assertEqual(camel_to_snake('CamelCaseWithSpecialCharacters'), 'camel_case_with_special_characters')
