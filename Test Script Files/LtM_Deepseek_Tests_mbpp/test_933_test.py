import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_simple_camel_to_snake(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')
        self.assertEqual(camel_to_snake('simpleCase'), 'simple_case')

    def test_edge_camel_to_snake(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('a'), 'a')
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('123'), '123')

    def test_boundary_camel_to_snake(self):
        self.assertEqual(camel_to_snake('AaBbCc'), 'a_a_b_b_c')
        self.assertEqual(camel_to_snake('aAaAaA'), 'a_a_a_a_a')
        self.assertEqual(camel_to_snake('ABCDEFGH'), 'a_b_c_d_e_f_g_h')

    def test_complex_camel_to_snake(self):
        self.assertEqual(camel_to_snake('complexCaseWithNumbers123'), 'complex_case_with_numbers_123')
        self.assertEqual(camel_to_snake('withSpecialChars$%^'), 'with_special_chars_')
