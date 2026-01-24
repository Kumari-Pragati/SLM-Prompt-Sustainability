import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_edge_case_single_char(self):
        self.assertEqual(remove_Char('a', 'a'), '')

    def test_edge_case_no_char(self):
        self.assertEqual(remove_Char('hello', 'z'), 'hello')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            remove_Char(None, 'a')

    def test_error_case_none_char(self):
        with self.assertRaises(TypeError):
            remove_Char('hello', None)
