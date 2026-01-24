import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_words(''), '')

    def test_single_word(self):
        self.assertEqual(reverse_words('hello'), 'hello')
        self.assertEqual(reverse_words('world'), 'world')

    def test_multiple_words(self):
        self.assertEqual(reverse_words('hello world'), 'world hello')
        self.assertEqual(reverse_words('apple banana'), 'banana apple')
        self.assertEqual(reverse_words('Python unittest'), 'unittest Python')

    def test_punctuation(self):
        self.assertEqual(reverse_words('hello, world!'), 'world! hello,')
        self.assertEqual(reverse_words('Python, unittest.'), '. unittest.Python')

    def test_whitespace(self):
        self.assertEqual(reverse_words('   hello   world   '), '   world   hello   ')
        self.assertEqual(reverse_words('   hello world   '), '   world   hello   ')
