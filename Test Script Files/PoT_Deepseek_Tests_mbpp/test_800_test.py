import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(remove_all_spaces(' '), '')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('Hello   World'), 'HelloWorld')

    def test_corner_case_spaces_at_ends(self):
        self.assertEqual(remove_all_spaces('   Hello World   '), 'HelloWorld')

    def test_corner_case_no_spaces(self):
        self.assertEqual(remove_all_spaces('HelloWorld'), 'HelloWorld')
