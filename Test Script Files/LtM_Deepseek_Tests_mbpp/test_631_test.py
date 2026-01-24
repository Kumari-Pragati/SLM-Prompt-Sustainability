import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_empty_input(self):
        self.assertEqual(replace_spaces(''), '')

    def test_input_with_spaces(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')
        self.assertEqual(replace_spaces('Python   Exercises'), 'Python_Exercises')

    def test_input_with_multiple_spaces(self):
        self.assertEqual(replace_spaces('Python   Exercises'), 'Python_Exercises')

    def test_input_with_special_characters(self):
        self.assertEqual(replace_spaces('Python@Exercises'), 'Python@Exercises')

    def test_input_with_numbers(self):
        self.assertEqual(replace_spaces('Python123Exercises'), 'Python123Exercises')

    def test_input_with_special_characters_and_spaces(self):
        self.assertEqual(replace_spaces('Python@ Exercises'), 'Python@_Exercises')
