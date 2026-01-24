import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate('hello world'), 'hello world')

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_duplicate_words(self):
        self.assertEqual(remove_duplicate('hello hello world world'), 'hello world')

    def test_special_characters(self):
        self.assertEqual(remove_duplicate('hello@world'), 'hello@world')

    def test_numbers_in_string(self):
        self.assertEqual(remove_duplicate('123 123 456 456'), '123 456')

    def test_case_sensitivity(self):
        self.assertEqual(remove_duplicate('Hello hello'), 'Hello')

    def test_whitespace_handling(self):
        self.assertEqual(remove_duplicate('  hello   world  '), 'hello world')
