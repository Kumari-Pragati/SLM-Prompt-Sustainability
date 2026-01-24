import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(replace_spaces(' '), '_')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('Multiple   Spaces'), 'Multiple_Spaces')

    def test_corner_case_no_spaces(self):
        self.assertEqual(replace_spaces('NoSpacesNeeded'), 'NoSpacesNeeded')
