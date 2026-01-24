import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case(self):
        self.assertEqual(replace_spaces(''), '')

    def test_corner_case(self):
        self.assertEqual(replace_spaces('a'), 'a')
        self.assertEqual(replace_spaces('Python'), 'Python')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)
