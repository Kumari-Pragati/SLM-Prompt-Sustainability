import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplChar(unittest.TestCase):

    def test_simple_text(self):
        self.assertEqual(remove_splchar('Hello World'), 'HelloWorld')

    def test_empty_text(self):
        self.assertEqual(remove_splchar(''), '')

    def test_text_with_special_characters(self):
        self.assertEqual(remove_splchar('Hello@World!'), 'HelloWorld')

    def test_text_with_underscores(self):
        self.assertEqual(remove_splchar('Hello_World'), 'HelloWorld')

    def test_text_with_numbers(self):
        self.assertEqual(remove_splchar('Hello123World'), 'Hello123World')

    def test_text_with_special_characters_and_numbers(self):
        self.assertEqual(remove_splchar('Hello@123World!'), 'Hello123World')
