import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_boundary_case_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_boundary_case_multiple_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_error_handling_none_input(self):
        with self.assertRaises(TypeError):
            remove_spaces(None)
