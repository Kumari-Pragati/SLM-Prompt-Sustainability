import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(first_repeated_word('hello'), 'hello')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word('hello world'), 'None')

    def test_repeated_word(self):
        self.assertEqual(first_repeated_word('hello hello world'), 'hello')

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_single_space(self):
        self.assertEqual(first_repeated_word('   '), 'None')

    def test_multiple_spaces(self):
        self.assertEqual(first_repeated_word('   hello   world   '), 'None')

    def test_repeated_word_at_start(self):
        self.assertEqual(first_repeated_word('hello hello world'), 'hello')

    def test_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word('hello world hello'), 'hello')

    def test_repeated_word_in_middle(self):
        self.assertEqual(first_repeated_word('hello world hello world'), 'hello')
