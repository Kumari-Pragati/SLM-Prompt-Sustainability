import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_all_spaces('Hello World'), 'HelloWorld')

    def test_edge_case_with_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('Hello   World'), 'HelloWorld')

    def test_edge_case_with_no_spaces(self):
        self.assertEqual(remove_all_spaces('HelloWorld'), 'HelloWorld')

    def test_edge_case_with_only_spaces(self):
        self.assertEqual(remove_all_spaces('   '), '')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(None)
