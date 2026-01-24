import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_duplicate('hello world hello'), 'hello world')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_duplicate_spaces(self):
        self.assertEqual(remove_duplicate('hello   world'), 'hello world')

    def test_special_characters(self):
        self.assertEqual(remove_duplicate('hello@world@hello'), 'hello@world')

    def test_numbers_and_letters(self):
        self.assertEqual(remove_duplicate('123hello123world123'), '123hello123world')

    def test_case_sensitivity(self):
        self.assertEqual(remove_duplicate('Hello World Hello'), 'Hello World')
