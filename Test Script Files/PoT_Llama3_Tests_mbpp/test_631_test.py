import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_no_spaces(self):
        self.assertEqual(replace_spaces(''), '')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces('a b'), 'a b')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('a   b'), 'a b')

    def test_edge_case_leading_spaces(self):
        self.assertEqual(replace_spaces('   a b'), 'a b')

    def test_edge_case_trailing_spaces(self):
        self.assertEqual(replace_spaces('a b   '), 'a b')

    def test_edge_case_mixed_spaces(self):
        self.assertEqual(replace_spaces('a b   c'), 'a b c')

    def test_edge_case_leading_and_trailing_spaces(self):
        self.assertEqual(replace_spaces('   a b   '), 'a b')
