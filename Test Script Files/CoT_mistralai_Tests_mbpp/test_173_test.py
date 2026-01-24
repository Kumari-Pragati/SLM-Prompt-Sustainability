import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_splchar(''), '')

    def test_single_char(self):
        for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            self.assertEqual(remove_splchar(char), char)

    def test_multiple_chars(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')

    def test_whitespace_only(self):
        self.assertEqual(remove_splchar('   \t\n\r  '), '')

    def test_special_characters(self):
        self.assertEqual(remove_splchar('!@#$%^&*()_+-=[]{};:'\'<>,.?/'), '')

    def test_mixed_case_and_special_chars(self):
        self.assertEqual(remove_splchar('Hello, World!@#$%^&*()_+-=[]{};:'\'<>,.?/'), 'Hello World')

    def test_multiline_text(self):
        text = '''Hello, World!
This is a test.
1234567890'''
        expected = 'Hello World\nThis is a test.\n1234567890'
        self.assertEqual(remove_splchar(text), expected)

    def test_unicode_string(self):
        text = 'Hello, 世界!'
        expected = 'Hello 世界'
        self.assertEqual(remove_splchar(text), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_splchar(123)
