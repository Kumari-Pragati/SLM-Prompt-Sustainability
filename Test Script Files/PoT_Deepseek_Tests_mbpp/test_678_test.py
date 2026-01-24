import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_corner_case_no_spaces(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')
