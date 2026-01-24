import unittest
from mbpp_482_code import match

class TestMatch(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(match('Abc'), 'Yes')

    def test_edge_case_empty_string(self):
        self.assertEqual(match(''), 'No')

    def test_boundary_case_single_capital_letter(self):
        self.assertEqual(match('A'), 'No')

    def test_boundary_case_single_lowercase_letter(self):
        self.assertEqual(match('a'), 'No')

    def test_complex_case_all_capital_letters(self):
        self.assertEqual(match('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'No')

    def test_complex_case_all_lowercase_letters(self):
        self.assertEqual(match('abcdefghijklmnopqrstuvwxyz'), 'No')

    def test_complex_case_mixed_case_letters(self):
        self.assertEqual(match('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'Yes')
