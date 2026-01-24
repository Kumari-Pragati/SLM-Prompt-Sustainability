import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_single_uppercase_letter(self):
        self.assertEqual(remove_lowercase('A'), 'A')

    def test_single_lowercase_letter(self):
        self.assertEqual(remove_lowercase('a'), '')

    def test_mixed_case_string(self):
        self.assertEqual(remove_lowercase('Hello, World!'), 'Hello, !')

    def test_multiple_spaces(self):
        self.assertEqual(remove_lowercase('   Hello   World   '), 'Hello   World   ')

    def test_special_characters(self):
        self.assertEqual(remove_lowercase('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/')

    def test_punctuation_and_lowercase(self):
        self.assertEqual(remove_lowercase('Hello, World!'), 'Hello, !')

    def test_punctuation_and_uppercase(self):
        self.assertEqual(remove_lowercase('Hello, World!'), 'Hello, !')
