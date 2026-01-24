import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_single_space(self):
        self.assertEqual(replace_spaces('Python Exercise'), 'Python_Exercise')

    def test_no_spaces(self):
        self.assertEqual(replace_spaces('PythonExercises'), 'PythonExercises')

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces('Python   Exercises'), 'Python_Exercises')

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_spaces_at_start_and_end(self):
        self.assertEqual(replace_spaces(' Python Exercises '), '_Python_Exercises_')

    def test_special_characters(self):
        self.assertEqual(replace_spaces('Py@th@n Exer@cises'), 'Py_th_n_Exer_cises')
