import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_single_char(self):
        self.assertEqual(remove_Char('hello', 'h'), 'ello')

    def test_no_occurrence(self):
        self.assertEqual(remove_Char('hello', 'z'), 'hello')

    def test_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_remove_all_chars(self):
        self.assertEqual(remove_Char('aaaaa', 'a'), '')

    def test_case_sensitivity(self):
        self.assertEqual(remove_Char('Hello', 'h'), 'Hello')

    def test_whitespace(self):
        self.assertEqual(remove_Char('hello world', ' '), 'helloworld')

    def test_edge_case_empty_char(self):
        self.assertEqual(remove_Char('hello', ''), 'hello')

    def test_edge_case_none_char(self):
        self.assertEqual(remove_Char('hello', None), 'hello')
