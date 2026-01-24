import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_edge_case_single_space(self):
        self.assertEqual(remove_multiple_spaces('Hello World'), 'Hello World')

    def test_boundary_case_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_corner_case_multiple_consecutive_spaces(self):
        self.assertEqual(remove_multiple_spaces('Hello      World'), 'Hello World')

    def test_corner_case_no_spaces(self):
        self.assertEqual(remove_multiple_spaces('HelloWorld'), 'HelloWorld')
