import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('Valid123Identifier'), 'valid123_identifier')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('_'), '_')
        self.assertEqual(camel_to_snake('__'), '__')
        self.assertEqual(camel_to_snake('_Identifier'), '_identifier')
        self.assertEqual(camel_to_snake('Identifier_'), 'identifier_')
        self.assertEqual(camel_to_snake('Identifier'), 'identifier')

    def test_boundary_cases(self):
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('Aa'), 'a_a')
        self.assertEqual(camel_to_snake('AaB'), 'a_a_b')
        self.assertEqual(camel_to_snake('AaBc'), 'a_a_b_c')
        self.assertEqual(camel_to_snake('AaBcD'), 'a_a_b_c_d')
        self.assertEqual(camel_to_snake('AaBcDe'), 'a_a_b_c_d_e')

    def test_special_cases(self):
        self.assertEqual(camel_to_snake('InvalidIdentifier123'), 'invalid_identifier123')
        self.assertEqual(camel_to_snake('Valid123Identifier'), 'valid123_identifier')
        self.assertEqual(camel_to_snake('ValidIdentifier123'), 'valid_identifier123')
