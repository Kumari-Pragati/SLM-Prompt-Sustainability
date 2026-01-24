import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'cherry']), 
                         [('apple', 2), ('banana', 1), ('cherry', 1)])

    def test_empty_input(self):
        self.assertEqual(count_common([]), [])

    def test_single_word_input(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_same_frequency_words(self):
        self.assertEqual(count_common(['apple', 'banana', 'cherry', 'banana']), 
                         [('banana', 2), ('apple', 1), ('cherry', 1)])

    def test_maximum_words(self):
        words = ['apple'] * 10000 + ['banana'] * 9999 + ['cherry'] * 9998
        self.assertEqual(count_common(words)[:3], [('apple', 10000), ('banana', 9999), ('cherry', 9998)])
