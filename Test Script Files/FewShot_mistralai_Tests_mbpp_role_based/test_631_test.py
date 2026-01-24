import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_replace_spaces_with_underscore(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(replace_spaces(' '), '_')

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces('Multiple Spaces'), 'Multiple_Spaces')

    def test_special_characters_before_space(self):
        self.assertEqual(replace_spaces('!Python Exercises'), '!Python_Exercises')

    def test_special_characters_after_space(self):
        self.assertEqual(replace_spaces('Python Exercises!'), 'Python_Exercises!')

    def test_special_characters_before_and_after_space(self):
        self.assertEqual(replace_spaces('!Python Exercises !'), '!Python_Exercises_')
