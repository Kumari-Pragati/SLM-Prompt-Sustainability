import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_simple_uppercase_and_lowercase(self):
        self.assertEqual(match('ABCdef'), 'Yes')
        self.assertEqual(match('abcDEF'), 'Yes')

    def test_edge_case_single_uppercase(self):
        self.assertEqual(match('ABC'), 'Yes')
        self.assertEqual(match('ABCdef '), 'No')

    def test_edge_case_single_lowercase(self):
        self.assertEqual(match('abc'), 'No')
        self.assertEqual(match('abc def'), 'No')

    def test_edge_case_no_letters(self):
        self.assertEqual(match('123'), 'No')
        self.assertEqual(match('_'), 'No')

    def test_edge_case_only_uppercase(self):
        self.assertEqual(match('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'Yes')

    def test_edge_case_only_lowercase(self):
        self.assertEqual(match('abcdefghijklmnopqrstuvwxyz'), 'Yes')

    def test_complex_case_mixed_case(self):
        self.assertEqual(match('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'Yes')

    def test_invalid_input_empty_string(self):
        self.assertEqual(match(''), 'No')
