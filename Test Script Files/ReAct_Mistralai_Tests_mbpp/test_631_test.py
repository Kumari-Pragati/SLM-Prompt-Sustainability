import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_replace_spaces_with_underscore(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_replace_spaces_with_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_replace_spaces_with_single_space(self):
        self.assertEqual(replace_spaces(' '), '_')

    def test_replace_spaces_with_multiple_spaces(self):
        self.assertEqual(replace_spaces('Multiple Spaces'), 'Multiple_Spaces')

    def test_replace_spaces_with_special_characters(self):
        self.assertEqual(replace_spaces('Python!Exercises'), 'Python!_Exercises')

    def test_replace_spaces_with_numbers(self):
        self.assertEqual(replace_spaces('Python 123 Exercises'), 'Python_123_Exercises')

    def test_replace_spaces_with_long_string(self):
        long_string = 'A' * 100 + ' B' * 100 + ' C' * 100
        self.assertEqual(replace_spaces(long_string), long_string.replace(' ', '_').replace('_', ' '))
