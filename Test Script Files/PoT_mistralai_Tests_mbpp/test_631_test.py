import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises_')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_edge_case_single_word(self):
        self.assertEqual(replace_spaces('Word'), 'Word')

    def test_edge_case_single_character(self):
        self.assertEqual(replace_spaces('A'), 'A')

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(replace_spaces(' Python Exercises '), 'Python_Exercises_')

    def test_edge_case_leading_trailing_underscores(self):
        self.assertEqual(replace_spaces('_Python_Exercises__'), 'PythonExercises')

    def test_edge_case_only_underscores(self):
        self.assertEqual(replace_spaces('__'), '__')

    def test_edge_case_only_spaces(self):
        self.assertEqual(replace_spaces('   '), '')
