import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_edge_case_single_space(self):
        self.assertEqual(remove_multiple_spaces('Hello World'), 'Hello World')

    def test_boundary_case_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_boundary_case_spaces_only(self):
        self.assertEqual(remove_multiple_spaces('   '), ' ')

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(None)
