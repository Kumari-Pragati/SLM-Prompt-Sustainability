import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('   Hello World   '), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces('H W'), 'HW')

    def test_no_spaces(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('Hello@World'), 'Hello@World')

    def test_numbers(self):
        self.assertEqual(remove_spaces('123 456'), '123456')
