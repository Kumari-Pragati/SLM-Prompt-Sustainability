import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_no_spaces(self):
        self.assertEqual(replace_spaces(''), '')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces('a'), 'a')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('a b c'), 'a_b_c')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            replace_spaces([])

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            replace_spaces(None)
