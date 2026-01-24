import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_char('hello', 'l', 'p'), 'heppo')

    def test_edge_case_no_change(self):
        self.assertEqual(replace_char('hello', 'x', 'p'), 'hello')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char('', 'x', 'p'), '')

    def test_edge_case_empty_char(self):
        self.assertEqual(replace_char('hello', '', 'p'), 'hello')

    def test_edge_case_empty_new_char(self):
        self.assertEqual(replace_char('hello', 'l', ''), 'heo')

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            replace_char(None, 'l', 'p')
