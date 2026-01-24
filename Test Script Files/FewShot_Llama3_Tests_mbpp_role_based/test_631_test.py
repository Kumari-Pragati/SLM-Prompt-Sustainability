import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces('Hello'), 'Hello')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('Hello   World'), 'Hello_World')

    def test_edge_case_multiple_spaces_with_leading_trailing_spaces(self):
        self.assertEqual(replace_spaces('   Hello   World   '), 'Hello_World')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)
