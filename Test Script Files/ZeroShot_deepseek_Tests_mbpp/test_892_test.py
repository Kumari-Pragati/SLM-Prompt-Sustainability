import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_single_space(self):
        self.assertEqual(remove_spaces('Hello World'), 'Hello World')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'Hello World')

    def test_trailing_spaces(self):
        self.assertEqual(remove_spaces('Hello World   '), 'Hello World')

    def test_leading_spaces(self):
        self.assertEqual(remove_spaces('   Hello World'), 'Hello World')

    def test_mixed_spaces(self):
        self.assertEqual(remove_spaces('   Hello   World   '), 'Hello World')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_no_spaces(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')
