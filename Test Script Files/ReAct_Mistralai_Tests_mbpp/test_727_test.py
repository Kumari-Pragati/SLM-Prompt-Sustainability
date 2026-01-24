import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')

    def test_single_char(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(remove_char(char), char)

    def test_multiple_chars(self):
        for word in ['hello', 'world', 'Python', 'Unittest', '1234567890']:
            self.assertEqual(remove_char(word), word.lower())

    def test_whitespace(self):
        self.assertEqual(remove_char('   \t\n\r  '), '')

    def test_punctuation(self):
        for punctuation in ['.', ',', '!', '?', ':', ';', '-', '_', '(', ')', '[', ']', '{', '}', '&', '@', '#', '%', '*', '+', '=', '|', '~', '^', '$', '`', '>', '<', '|', '\\', '/']:
            self.assertEqual(remove_char(punctuation), '')

    def test_mixed_case(self):
        self.assertEqual(remove_char('HeLlO wOrLd'), 'helloworld')

    def test_special_characters(self):
        for special in ['@#$%^&*()_+-=[]{}|\\/', '!@#$%^&*()_+-=[]{}|\\/', 'HeLlO wOrLd@#$%^&*()_+-=[]{}|\\/', 'HeLlO wOrLd!@#$%^&*()_+-=[]{}|\\/']:
            self.assertEqual(remove_char(special), special.lower().replace(' ', ''))

    def test_empty_list(self):
        self.assertEqual(remove_char([]), '')

    def test_list_with_single_char(self):
        self.assertEqual(remove_char(['a']), 'a')

    def test_list_with_multiple_chars(self):
        self.assertEqual(remove_char(['a', 'b', 'c']), 'abc')

    def test_list_with_special_characters(self):
        self.assertEqual(remove_char(['@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '[', ']', '{', '}', '|', '\\', '/']), '')

    def test_list_with_whitespace(self):
        self.assertEqual(remove_char(['   \t\n\r  ']), '')

    def test_list_with_punctuation(self):
        self.assertEqual(remove_char(['.', ',', '!', '?', ':', ';', '-', '_', '(', ')', '[', ']', '{', '}', '&', '@', '#', '%', '*', '+', '=', '|', '~', '^', '$', '`', '>', '<', '|', '\\', '/']), [])
