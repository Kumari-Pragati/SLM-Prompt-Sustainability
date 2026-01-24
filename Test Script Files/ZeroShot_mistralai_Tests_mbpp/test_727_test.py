import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')

    def test_single_char(self):
        self.assertEqual(remove_char('a'), 'a')
        self.assertEqual(remove_char('A'), 'A')
        self.assertEqual(remove_char('0'), '0')

    def test_multiple_chars(self):
        self.assertEqual(remove_char('Hello'), 'Hello')
        self.assertEqual(remove_char('World'), 'World')
        self.assertEqual(remove_char('12345'), '12345')

    def test_special_characters(self):
        self.assertEqual(remove_char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '')

    def test_whitespace(self):
        self.assertEqual(remove_char('   Hello   '), 'Hello')

    def test_numbers_with_special_characters(self):
        self.assertEqual(remove_char('123-456-7890'), '1234567890')

    def test_mixed_case(self):
        self.assertEqual(remove_char('HeLlO wOrLd'), 'helloworld')

    def test_underscores(self):
        self.assertEqual(remove_char('_Hello_'), 'Hello')
        self.assertEqual(remove_char('_HeLlO_'), 'HeLlo')
