import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_edge_case_single_char(self):
        self.assertEqual(remove_spaces('a'), 'a')

    def test_edge_case_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces(' hello world '), 'helloworld')

    def test_edge_case_only_spaces(self):
        self.assertEqual(remove_spaces('   '), '')
