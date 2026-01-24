import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(reverse_words('hello'), 'hello')

    def test_multiple_words(self):
        self.assertEqual(reverse_words('hello world'), 'world hello')

    def test_empty_string(self):
        self.assertEqual(reverse_words(''), '')

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(reverse_words('   hello world   '), 'world hello')

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_words('hello$world'), 'world$hello')

    def test_string_with_numbers(self):
        self.assertEqual(reverse_words('123 456'), '456 123')
