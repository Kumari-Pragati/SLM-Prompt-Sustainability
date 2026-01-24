import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_replace_spaces(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')
        self.assertEqual(replace_spaces('Hello World'), 'Hello_World')
        self.assertEqual(replace_spaces(''), '')
        self.assertEqual(replace_spaces('No spaces'), 'No_spaces')
        self.assertEqual(replace_spaces('Multiple spaces   '), 'Multiple_spaces')
        self.assertEqual(replace_spaces('No spaces at all'), 'No_spaces_at_all')

    def test_replace_spaces_with_multiple_spaces(self):
        self.assertEqual(replace_spaces('Hello   World'), 'Hello_World')
        self.assertEqual(replace_spaces('Multiple   spaces'), 'Multiple_spaces')

    def test_replace_spaces_with_leading_spaces(self):
        self.assertEqual(replace_spaces('   Hello World'), 'Hello_World')

    def test_replace_spaces_with_trailing_spaces(self):
        self.assertEqual(replace_spaces('Hello World   '), 'Hello_World')

    def test_replace_spaces_with_leading_and_trailing_spaces(self):
        self.assertEqual(replace_spaces('   Hello World   '), 'Hello_World')
