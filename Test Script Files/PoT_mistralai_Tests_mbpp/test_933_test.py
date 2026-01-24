import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('Valid_Identifier'), 'valid_identifier')

    def test_edge_case_uppercase_first_char(self):
        self.assertEqual(camel_to_snake('UpperCase'), 'upper_case')
        self.assertEqual(camel_to_snake('UPPER_CASE'), 'upper_case')

    def test_edge_case_uppercase_middle_char(self):
        self.assertEqual(camel_to_snake('MiddleCase'), 'middle_case')
        self.assertEqual(camel_to_snake('Middle_Case'), 'middle_case')

    def test_edge_case_uppercase_end_char(self):
        self.assertEqual(camel_to_snake('EndCase'), 'end_case')
        self.assertEqual(camel_to_snake('End_Case'), 'end_case')

    def test_edge_case_uppercase_all_chars(self):
        self.assertEqual(camel_to_snake('ALL_CAPS'), 'all_caps')

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_edge_case_single_char(self):
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('_'), '_')

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(camel_to_snake('__'), '__')
        self.assertEqual(camel_to_snake('___'), '__')

    def test_edge_case_numbers(self):
        self.assertEqual(camel_to_snake('123Camel'), '123_camel')
        self.assertEqual(camel_to_snake('Camel123'), 'camel_123')
        self.assertEqual(camel_to_snake('123_Camel'), '123_camel')
        self.assertEqual(camel_to_snake('Camel_123'), 'camel_123')

    def test_edge_case_numbers_and_underscores(self):
        self.assertEqual(camel_to_snake('1_2_3_Camel'), '1_2_3_camel')
        self.assertEqual(camel_to_snake('Camel1_2_3'), 'camel_1_2_3')
        self.assertEqual(camel_to_snake('1_2_3_camel'), '1_2_3_camel')
        self.assertEqual(camel_to_snake('camel1_2_3'), 'camel_1_2_3')
