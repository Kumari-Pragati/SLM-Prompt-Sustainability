import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSpecialCharacters(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')

    def test_empty_string(self):
        self.assertEqual(remove_splchar(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(remove_splchar('Hello123World456'), 'HelloWorld')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_splchar('Hello@World#'), 'HelloWorld')

    def test_string_with_underscores(self):
        self.assertEqual(remove_splchar('Hello_World_Is_Great'), 'HelloWorldIsGreat')

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_splchar('HelloWorLD'), 'HelloWorLD')

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(remove_splchar('   Hello World   '), 'HelloWorld')

    def test_string_with_multiple_consecutive_special_characters(self):
        self.assertEqual(remove_splchar('Hello,,,World!!!'), 'HelloWorld')

    def test_string_with_special_characters_and_numbers(self):
        self.assertEqual(remove_splchar('Hello@123World456!!!'), 'Hello123World456')
