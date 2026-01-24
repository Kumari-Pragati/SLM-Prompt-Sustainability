import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_lowercase_string(self):
        self.assertEqual(remove_uppercase('hello'), 'hello')

    def test_mixed_case_string(self):
        self.assertEqual(remove_uppercase('HeLlO wOrLd'), 'helloworld')

    def test_all_uppercase_string(self):
        self.assertEqual(remove_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '')

    def test_special_characters(self):
        self.assertEqual(remove_uppercase('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/')

    def test_whitespace_only_string(self):
        self.assertEqual(remove_uppercase('   '), '   ')
