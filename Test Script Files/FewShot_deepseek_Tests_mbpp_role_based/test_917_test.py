import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_uppercase_lowercase('AbCdEfGhI'), 'Found a match!')

    def test_boundary_conditions(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('ABCDEFGHI'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('abcdefghi'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_uppercase_lowercase('Abcdefghi'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 'Not matched!')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(['AbCdEfGhI'])
