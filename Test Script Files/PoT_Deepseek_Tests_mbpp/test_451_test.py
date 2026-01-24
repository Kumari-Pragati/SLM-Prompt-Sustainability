import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_whitespaces('Hello World'), 'HelloWorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_whitespaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(remove_whitespaces(' '), '')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(remove_whitespaces('Hello   World'), 'HelloWorld')

    def test_corner_case_newlines(self):
        self.assertEqual(remove_whitespaces('Hello\nWorld'), 'HelloWorld')

    def test_corner_case_tabs(self):
        self.assertEqual(remove_whitespaces('Hello\tWorld'), 'HelloWorld')
