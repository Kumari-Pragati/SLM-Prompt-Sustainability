import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(remove_char('Python3.8'), 'Python38')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_char('Python@3.8'), 'Python38')

    def test_string_with_spaces(self):
        self.assertEqual(remove_char('Hello World'), 'HelloWorld')

    def test_string_with_underscores(self):
        self.assertEqual(remove_char('Hello_World'), 'HelloWorld')

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_char('Hello WoRlD'), 'HelloWorld')

    def test_string_with_lowercase_letters(self):
        self.assertEqual(remove_char('hello world'), 'helloworld')

    def test_string_with_uppercase_letters(self):
        self.assertEqual(remove_char('HELLO WORLD'), 'HELLOWORLD')

    def test_string_with_mixed_case_and_special_characters(self):
        self.assertEqual(remove_char('HeLLo WoRlD!'), 'HeLLoWoRlD')
