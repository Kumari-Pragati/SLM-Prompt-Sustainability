import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_simple_replace_spaces(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_empty_input(self):
        self.assertEqual(replace_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(replace_spaces('Hello'), 'Hello')

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces('Hello   World'), 'Hello_World')

    def test_multiple_spaces_with_newline(self):
        self.assertEqual(replace_spaces('Hello   \nWorld'), 'Hello_World')

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(replace_spaces('   Hello   '), '_Hello_')
