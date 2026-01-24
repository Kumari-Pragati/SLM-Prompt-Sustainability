import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('ValidIdentifier'), 'valid_identifier')
        self.assertEqual(camel_to_snake('VariableName'), 'variable_name')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('_'), '_')
        self.assertEqual(camel_to_snake('__'), '__')
        self.assertEqual(camel_to_snake('___'), '___')
        self.assertEqual(camel_to_snake('_Identifier'), '_identifier')
        self.assertEqual(camel_to_snake('Identifier_'), 'identifier_')
        self.assertEqual(camel_to_snake('Identifier__'), 'identifier__')
        self.assertEqual(camel_to_snake('__Identifier'), '__identifier')

    def test_boundary_cases(self):
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('Aa'), 'a_a')
        self.assertEqual(camel_to_snake('AaB'), 'a_a_b')
        self.assertEqual(camel_to_snake('AaBc'), 'a_a_b_c')
        self.assertEqual(camel_to_snake('AaBcD'), 'a_a_b_c_d')
        self.assertEqual(camel_to_snake('AaBcDe'), 'a_a_b_c_d_e')
        self.assertEqual(camel_to_snake('AaBcDeF'), 'a_a_b_c_d_e_f')
        self.assertEqual(camel_to_snake('AaBcDeFg'), 'a_a_b_c_d_e_f_g')
        self.assertEqual(camel_to_snake('AaBcDeFgH'), 'a_a_b_c_d_e_f_g_h')
        self.assertEqual(camel_to_snake('AaBcDeFgHi'), 'a_a_b_c_d_e_f_g_h_i')
