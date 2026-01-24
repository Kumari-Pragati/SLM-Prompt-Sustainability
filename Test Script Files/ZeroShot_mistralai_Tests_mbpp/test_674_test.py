import unittest
from mbpp_674_code import OrderedDict
from your_module import remove_duplicate  # Assuming the function is in a module named 'your_module'

class TestRemoveDuplicate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word(self):
        self.assertEqual(remove_duplicate('hello'), 'hello')

    def test_multiple_words(self):
        self.assertEqual(remove_duplicate('hello world hello'), 'hello world')

    def test_duplicate_words(self):
        self.assertEqual(remove_duplicate('hello hello world hello'), 'hello world')

    def test_case_insensitive(self):
        self.assertEqual(remove_duplicate('Hello World Hello'), 'Hello World')

    def test_punctuation(self):
        self.assertEqual(remove_duplicate('hello, world!'), 'hello world')

    def test_numbers(self):
        self.assertEqual(remove_duplicate('1 2 3 4 5 6'), '1 2 3 4 5 6')

    def test_mixed_case_and_numbers(self):
        self.assertEqual(remove_duplicate('Hello 123 World'), 'Hello World')
