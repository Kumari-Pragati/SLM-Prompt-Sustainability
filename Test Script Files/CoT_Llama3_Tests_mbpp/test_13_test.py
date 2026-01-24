import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_common([]), [])

    def test_single_word(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_multiple_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange']), [('apple', 2), ('banana', 1), ('orange', 1)])

    def test_multiple_words_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'apple', 'banana', 'banana', 'orange']), [('apple', 2), ('banana', 2), ('orange', 1)])

    def test_top_four_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange', 'apple', 'banana', 'banana']), [('apple', 3), ('banana', 3), ('orange', 1)])

    def test_top_four_words_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'apple', 'apple', 'banana', 'banana', 'banana', 'orange']), [('apple', 3), ('banana', 3), ('orange', 1)])

    def test_top_four_words_with_less_than_four_unique_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'banana']), [('apple', 2), ('banana', 2)])

    def test_top_four_words_with_less_than_four_unique_words_and_duplicates(self):
        self.assertEqual(count_common(['apple', 'apple', 'apple', 'banana', 'banana', 'banana']), [('apple', 3), ('banana', 3)])
