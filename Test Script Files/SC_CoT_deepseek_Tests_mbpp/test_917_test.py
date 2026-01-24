import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_uppercase_lowercase('AbcDef'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_uppercase_lowercase('abcdef'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_uppercase_lowercase('ABC'), 'Not matched!')

    def test_special_case(self):
        self.assertEqual(text_uppercase_lowercase('AbCdEfGh'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(12345)
