import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')

    def test_empty_input(self):
        self.assertEqual(remove_spaces(''), '')

    def test_input_with_special_characters(self):
        self.assertEqual(remove_spaces('hello@world'), 'helloworld')

    def test_input_with_numbers(self):
        self.assertEqual(remove_spaces('123 456'), '123456')

    def test_input_with_multiple_spaces(self):
        self.assertEqual(remove_spaces('hello   world'), 'helloworld')

    def test_input_with_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('   hello world   '), 'helloworld')
