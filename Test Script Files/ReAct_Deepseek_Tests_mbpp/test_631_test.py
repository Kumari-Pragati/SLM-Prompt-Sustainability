import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        text = 'Python Exercises'
        expected_output = 'Python_Exercises'
        self.assertEqual(replace_spaces(text), expected_output)

    def test_edge_case_with_no_spaces(self):
        text = 'PythonExercises'
        expected_output = 'PythonExercises'
        self.assertEqual(replace_spaces(text), expected_output)

    def test_edge_case_with_multiple_spaces(self):
        text = 'Python   Exercises'
        expected_output = 'Python_Exercises'
        self.assertEqual(replace_spaces(text), expected_output)

    def test_edge_case_with_trailing_spaces(self):
        text = 'Python Exercises   '
        expected_output = 'Python_Exercises_'
        self.assertEqual(replace_spaces(text), expected_output)

    def test_edge_case_with_leading_spaces(self):
        text = '   Python Exercises'
        expected_output = '_Python_Exercises'
        self.assertEqual(replace_spaces(text), expected_output)

    def test_edge_case_with_empty_string(self):
        text = ''
        expected_output = ''
        self.assertEqual(replace_spaces(text), expected_output)
