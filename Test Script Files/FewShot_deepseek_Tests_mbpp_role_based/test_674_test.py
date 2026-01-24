import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_duplicate('hello world'), 'hello world')

    def test_typical_use_case_with_duplicates(self):
        self.assertEqual(remove_duplicate('hello hello world world'), 'hello world')

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_special_characters(self):
        self.assertEqual(remove_duplicate('!@#$%^&*()'), '!@#$%^&*()')

    def test_numbers_and_letters(self):
        self.assertEqual(remove_duplicate('123abc123abc'), '123abc')

    def test_whitespace_only(self):
        self.assertEqual(remove_duplicate('   '), '   ')

    def test_mixed_case(self):
        self.assertEqual(remove_duplicate('Hello World'), 'Hello World')
