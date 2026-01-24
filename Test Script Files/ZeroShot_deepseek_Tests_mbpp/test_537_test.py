import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(first_repeated_word('hello'), 'None')

    def test_no_repeat(self):
        self.assertEqual(first_repeated_word('hello world'), 'None')

    def test_repeat_at_start(self):
        self.assertEqual(first_repeated_word('hello hello world'), 'hello')

    def test_repeat_in_middle(self):
        self.assertEqual(first_repeated_word('hello world world'), 'world')

    def test_repeat_at_end(self):
        self.assertEqual(first_repeated_word('hello world goodbye world'), 'world')

    def test_case_insensitive(self):
        self.assertEqual(first_repeated_word('Hello hello world'), 'Hello')

    def test_punctuation(self):
        self.assertEqual(first_repeated_word('hello, hello world'), 'hello')
        self.assertEqual(first_repeated_word('hello world! hello'), 'hello')
