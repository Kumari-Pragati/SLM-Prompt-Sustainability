import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(remove_duplicate('hello world'), 'hello world')

    def test_duplicate_string(self):
        self.assertEqual(remove_duplicate('hello hello'), 'hello')

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(''), '')

    def test_single_word_string(self):
        self.assertEqual(remove_duplicate('python'), 'python')

    def test_special_characters_string(self):
        self.assertEqual(remove_duplicate('!@#$%^&*()'), '!@#$%^&*()')

    def test_duplicate_words_with_special_characters(self):
        self.assertEqual(remove_duplicate('hello world! world!'), 'hello world!')

    def test_duplicate_words_with_numbers(self):
        self.assertEqual(remove_duplicate('1 2 1 2 3 3'), '1 2 3')

    def test_duplicate_words_with_mixed_case(self):
        self.assertEqual(remove_duplicate('Hello HELLO'), 'Hello')
