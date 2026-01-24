import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_condition(self):
        self.assertEqual(replace_spaces(''), '')

    def test_boundary_condition(self):
        self.assertEqual(replace_spaces('P' * 1000), 'P' * 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)
