import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_splchar(''), '')

    def test_single_char(self):
        self.assertEqual(remove_splchar('a'), 'a')

    def test_multiple_chars(self):
        self.assertEqual(remove_splchar('Hello World'), 'HelloWorld')

    def test_mixed_case(self):
        self.assertEqual(remove_splchar('HeLlO wOrLd'), 'HelloWorld')

    def test_whitespace(self):
        self.assertEqual(remove_splchar(' Hello World '), 'HelloWorld')

    def test_special_characters(self):
        self.assertEqual(remove_splchar('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '')

    def test_numbers(self):
        self.assertEqual(remove_splchar('1234567890'), '1234567890')

    def test_punctuation(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'HelloWorld')
