import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_spaces_at_beginning(self):
        self.assertEqual(replace_spaces('  Python Exercises'), 'Python_Exercises')

    def test_edge_case_spaces_at_end(self):
        self.assertEqual(replace_spaces('Python Exercises  '), 'Python_Exercises ')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('Python   Exercises'), 'Python_Exercises')

    def test_edge_case_no_spaces(self):
        self.assertEqual(replace_spaces('PythonExercises'), 'PythonExercises')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_multiple_spaces_at_beginning(self):
        self.assertEqual(replace_spaces('   Python Exercises'), 'Python_Exercises')

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(replace_spaces('Python Exercises   '), 'Python_Exercises ')

    def test_edge_case_spaces_and_underscores(self):
        self.assertEqual(replace_spaces('Python _ Exercises'), 'Python__Exercises')

    def test_edge_case_underscores_and_spaces(self):
        self.assertEqual(replace_spaces('Python Exercises_'), 'Python_Exercises')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            replace_spaces(None)
