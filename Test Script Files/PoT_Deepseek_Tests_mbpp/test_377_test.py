import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_boundary_case_single_char(self):
        self.assertEqual(remove_Char('a', 'a'), '')

    def test_corner_case_repeated_char(self):
        self.assertEqual(remove_Char('aaa', 'a'), '')

    def test_corner_case_non_existing_char(self):
        self.assertEqual(remove_Char('hello', 'z'), 'hello')

    def test_corner_case_multiple_occurrences(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')
