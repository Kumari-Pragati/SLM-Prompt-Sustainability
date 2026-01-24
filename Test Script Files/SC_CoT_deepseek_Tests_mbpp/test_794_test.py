import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_edge_case_no_characters(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_edge_case_only_a(self):
        self.assertEqual(text_starta_endb('ab'), 'Not matched!')
        self.assertEqual(text_starta_endb('aab'), 'Not matched!')

    def test_edge_case_only_b(self):
        self.assertEqual(text_starta_endb('ba'), 'Not matched!')
        self.assertEqual(text_starta_endb('bba'), 'Not matched!')

    def test_corner_case_a_before_b(self):
        self.assertEqual(text_starta_endb('bbaa'), 'Not matched!')

    def test_corner_case_multiple_a_multiple_b(self):
        self.assertEqual(text_starta_endb('abcabc'), 'Found a match!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_starta_endb(123)
