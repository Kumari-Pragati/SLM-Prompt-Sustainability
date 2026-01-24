import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(remove_char('1234567890'), '1234567890')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_char('!@#$%^&*()'), '')

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_char('Hello, World!1234567890!@#$%^&*()'), 'HelloWorld1234567890')

    def test_string_with_underscore(self):
        self.assertEqual(remove_char('Hello_World'), 'HelloWorld')

    def test_string_with_whitespace(self):
        self.assertEqual(remove_char('Hello World'), 'HelloWorld')
