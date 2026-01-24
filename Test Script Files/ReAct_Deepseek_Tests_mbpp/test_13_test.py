import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_case(self):
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']
        result = count_common(words)
        self.assertEqual(result, [('cherry', 3), ('banana', 2), ('apple', 2)])

    def test_single_word(self):
        words = ['apple']
        result = count_common(words)
        self.assertEqual(result, [('apple', 1)])

    def test_empty_list(self):
        words = []
        result = count_common(words)
        self.assertEqual(result, [])

    def test_all_same_words(self):
        words = ['apple', 'apple', 'apple', 'apple']
        result = count_common(words)
        self.assertEqual(result, [('apple', 4)])

    def test_top_four_less_than_four(self):
        words = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'date', 'apple']
        result = count_common(words)
        self.assertEqual(result, [('apple', 3), ('banana', 2), ('cherry', 2), ('date', 2)])

    def test_top_four_exactly_four(self):
        words = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'date', 'fig', 'fig']
        result = count_common(words)
        self.assertEqual(result, [('fig', 2), ('apple', 2), ('banana', 2), ('cherry', 2)])
