import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_edge_case_with_lowercase_only(self):
        self.assertEqual(match('helloworld'), 'No')

    def test_edge_case_with_uppercase_only(self):
        self.assertEqual(match('HELLOWORLD'), 'No')

    def test_edge_case_with_numeric_characters(self):
        self.assertEqual(match('HelloWorld123'), 'No')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(match('Hello@World'), 'No')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(match(''), 'No')
