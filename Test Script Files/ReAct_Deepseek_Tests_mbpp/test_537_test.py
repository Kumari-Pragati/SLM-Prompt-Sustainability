import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_word('hello world hello'), 'hello')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word('unique words'), 'None')

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_repeated_word_with_punctuation(self):
        self.assertEqual(first_repeated_word('hello, world hello'), 'hello')

    def test_case_sensitivity(self):
        self.assertEqual(first_repeated_word('Hello World hello'), 'Hello')

    def test_whitespace_only(self):
        self.assertEqual(first_repeated_word('   '), 'None')

    def test_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word('first second third second'), 'second')
