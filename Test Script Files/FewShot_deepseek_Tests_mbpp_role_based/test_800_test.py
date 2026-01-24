import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(remove_all_spaces(' '), '')

    def test_boundary_case_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('   '), '')

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(None)
