import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_first_repeated_word(self):
        self.assertEqual(first_repeated_word("hello world hello"), "hello")
        self.assertEqual(first_repeated_word("hello world"), 'None')
        self.assertEqual(first_repeated_word("hello hello world"), "hello")
        self.assertEqual(first_repeated_word("hello world world"), 'None')
        self.assertEqual(first_repeated_word("hello"), 'None')
        self.assertEqual(first_repeated_word("hello hello hello"), "hello")
        self.assertEqual(first_repeated_word("hello world hello world"), "hello")
        self.assertEqual(first_repeated_word("hello world world"), 'None')
