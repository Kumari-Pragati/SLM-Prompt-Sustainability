import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_common([]), [])

    def test_single_word(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_multiple_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'banana', 'apple']), [('apple', 3), ('banana', 2)])

    def test_multiple_words_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'banana', 'apple', 'apple']), [('apple', 4), ('banana', 2)])

    def test_multiple_words_with_duplicates_and_duplicates(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'banana', 'apple', 'apple', 'banana', 'banana']), [('apple', 4), ('banana', 4)])

    def test_multiple_words_with_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'banana', 'apple', 'apple', 'apple', 'banana', 'banana', 'banana']), [('apple', 4), ('banana', 4)])
