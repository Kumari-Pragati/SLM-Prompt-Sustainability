import unittest
from mbpp_13_code import Counter
from 13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_four_words(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana']
        result = count_common(words)
        self.assertEqual(result, [('apple', 2), ('banana', 2)])

    def test_one_word(self):
        words = ['apple']
        result = count_common(words)
        self.assertEqual(result, [('apple', 1)])

    def test_empty_list(self):
        words = []
        result = count_common(words)
        self.assertEqual(result, [])

    def test_single_word_count(self):
        words = ['apple'] * 5
        result = count_common(words)
        self.assertEqual(result, [('apple', 5)])

    def test_multiple_unique_words(self):
        words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
        result = count_common(words)
        self.assertEqual(result, [('apple', 1), ('banana', 1), ('orange', 1), ('grape', 1), ('kiwi', 1)])
