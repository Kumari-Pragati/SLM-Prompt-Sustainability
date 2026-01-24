import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_replace_spaces_with_underscores(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_replace_multiple_spaces_with_underscores(self):
        self.assertEqual(replace_spaces('Multiple Spaces'), 'Multiple_Spaces')

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_single_character(self):
        self.assertEqual(replace_spaces('A'), 'A')

    def test_leading_trailing_spaces(self):
        self.assertEqual(replace_spaces(' leading spaces   trailing spaces'), 'leading_spaces_trailing_spaces')

    def test_special_characters(self):
        self.assertEqual(replace_spaces('Python!Exercises'), 'Python!_Exercises')

    def test_spaces_after_special_characters(self):
        self.assertEqual(replace_spaces('Exercises!'), 'Exercises!_')

    def test_spaces_before_special_characters(self):
        self.assertEqual(replace_spaces('!Python Exercises'), '!_Python_Exercises')

    def test_spaces_before_and_after_special_characters(self):
        self.assertEqual(replace_spaces('!Python! Exercises!'), '!_Python!_Exercises_')

    def test_only_special_characters(self):
        self.assertEqual(replace_spaces('!@#$%^&*()'), '!_@#$%^&*(_)')

    def test_only_underscores(self):
        self.assertEqual(replace_spaces('__'), '__')
