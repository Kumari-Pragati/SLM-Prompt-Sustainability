import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_whitespaces('Hello World'), 'HelloWorld')

    def test_edge_condition(self):
        self.assertEqual(remove_whitespaces(''), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_whitespaces(' '), '')

    def test_multiple_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello   World'), 'HelloWorld')

    def test_new_line_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello\nWorld'), 'HelloWorld')

    def test_tab_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello\tWorld'), 'HelloWorld')

    def test_mixed_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello   \t\n World'), 'HelloWorld')
