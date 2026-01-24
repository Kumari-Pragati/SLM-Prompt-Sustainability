import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')

    def test_single_letter(self):
        self.assertEqual(remove_char('a'), 'a')

    def test_multiple_letters(self):
        self.assertEqual(remove_char('Hello'), 'Hello')

    def test_mixed_string(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')

    def test_whitespace_only(self):
        self.assertEqual(remove_char('   '), '')

    def test_special_characters(self):
        self.assertEqual(remove_char('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '')

    def test_underscore(self):
        self.assertEqual(remove_char('_'), '')

    def test_number(self):
        self.assertEqual(remove_char('12345'), '12345')

    def test_number_with_special_characters(self):
        self.assertEqual(remove_char('123!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '123')
