import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_whitespaces('Hello World'), 'HelloWorld')

    def test_edge_case(self):
        self.assertEqual(remove_whitespaces(''), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces('Hello   World'), 'HelloWorld')

    def test_tab_spaces(self):
        self.assertEqual(remove_whitespaces('Hello\tWorld'), 'HelloWorld')

    def test_new_line_spaces(self):
        self.assertEqual(remove_whitespaces('Hello\nWorld'), 'HelloWorld')

    def test_special_characters(self):
        self.assertEqual(remove_whitespaces('Hello@#$%^&*()World'), 'Hello@#$%^&*()World')

    def test_numeric_characters(self):
        self.assertEqual(remove_whitespaces('Hello12345World'), 'Hello12345World')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(12345)
