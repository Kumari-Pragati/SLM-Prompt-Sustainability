import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_simple_space_replacement(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_multiple_spaces_replacement(self):
        self.assertEqual(replace_spaces('Multiple Spaces'), 'Multiple_Spaces')

    def test_single_space_removal(self):
        self.assertEqual(replace_spaces('Single'), 'Single')

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_special_characters_preservation(self):
        self.assertEqual(replace_spaces('Python#Exercises'), 'Python#Exercises')

    def test_space_after_special_character_replacement(self):
        self.assertEqual(replace_spaces('_Python Exercises'), 'Python_Exercises')

    def test_space_before_special_character_replacement(self):
        self.assertEqual(replace_spaces('Python_ Exercises'), 'Python_Exercises')
