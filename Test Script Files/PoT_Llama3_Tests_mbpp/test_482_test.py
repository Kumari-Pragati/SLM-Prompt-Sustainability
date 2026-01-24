import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_edge_case_uppercase(self):
        self.assertEqual(match('HELLO'), 'No')

    def test_edge_case_lowercase(self):
        self.assertEqual(match('hello'), 'No')

    def test_edge_case_mixed(self):
        self.assertEqual(match('Hello'), 'No')

    def test_edge_case_empty(self):
        self.assertEqual(match(''), 'No')

    def test_edge_case_single_uppercase(self):
        self.assertEqual(match('A'), 'No')

    def test_edge_case_single_lowercase(self):
        self.assertEqual(match('a'), 'No')

    def test_edge_case_single_mixed(self):
        self.assertEqual(match('a'), 'No')

    def test_edge_case_multiple_uppercase(self):
        self.assertEqual(match('ABC'), 'No')

    def test_edge_case_multiple_lowercase(self):
        self.assertEqual(match('abc'), 'No')

    def test_edge_case_multiple_mixed(self):
        self.assertEqual(match('AbC'), 'No')

    def test_edge_case_spaces(self):
        self.assertEqual(match('Hello World'), 'No')

    def test_edge_case_punctuation(self):
        self.assertEqual(match('Hello!'), 'No')

    def test_edge_case_numbers(self):
        self.assertEqual(match('Hello123'), 'No')

    def test_edge_case_special_chars(self):
        self.assertEqual(match('Hello@'), 'No')
