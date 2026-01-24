import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_replace_spaces(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')
        self.assertEqual(replace_spaces('Hello World'), 'Hello_World')
        self.assertEqual(replace_spaces('This is a test'), 'This_is_a_test')
        self.assertEqual(replace_spaces('Replace all spaces'), 'Replace_all_spaces')
