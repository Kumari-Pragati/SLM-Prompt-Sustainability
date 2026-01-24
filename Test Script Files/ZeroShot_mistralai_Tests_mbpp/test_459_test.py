import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_single_uppercase_letter(self):
        self.assertEqual(remove_uppercase('A'), '')

    def test_single_lowercase_letter(self):
        self.assertEqual(remove_uppercase('a'), 'a')

    def test_mixed_case_string(self):
        self.assertEqual(remove_uppercase('Hello World'), 'helloworld')

    def test_multiple_uppercase_letters(self):
        self.assertEqual(remove_uppercase('ABCDEFG'), 'cdefg')

    def test_special_characters(self):
        self.assertEqual(remove_uppercase('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/')

    def test_punctuation_and_uppercase(self):
        self.assertEqual(remove_uppercase('Hello, World!'), 'helloworld')
