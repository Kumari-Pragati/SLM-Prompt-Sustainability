import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_replace_spaces_with_underscores(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_replace_underscores_with_spaces(self):
        self.assertEqual(replace_spaces('Python_Exercises'), 'Python Exercises')

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(replace_spaces(' '), '_')

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces('Multiple Spaces'), 'Multiple_Spaces')

    def test_special_characters_and_spaces(self):
        self.assertEqual(replace_spaces('Python!Exercises'), 'Python!_Exercises')
