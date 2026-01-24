import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_whitespaces('Hello World'), 'HelloWorld')

    def test_edge_case_with_multiple_spaces(self):
        self.assertEqual(remove_whitespaces('Hello   World'), 'HelloWorld')

    def test_edge_case_with_tabs(self):
        self.assertEqual(remove_whitespaces('Hello\tWorld'), 'HelloWorld')

    def test_edge_case_with_newlines(self):
        self.assertEqual(remove_whitespaces('Hello\nWorld'), 'HelloWorld')

    def test_edge_case_with_mixed_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello   \t\n World'), 'HelloWorld')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(None)
