import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_single_space_removal(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_multiple_spaces_removal(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_leading_trailing_spaces_removal(self):
        self.assertEqual(remove_spaces('   Hello World   '), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space_string(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_no_spaces_string(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')

    def test_special_characters_spaces_removal(self):
        self.assertEqual(remove_spaces('Hello!! World!!'), 'Hello!!World!!')
