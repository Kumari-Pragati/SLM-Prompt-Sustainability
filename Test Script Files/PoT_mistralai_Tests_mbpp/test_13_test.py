import unittest
from mbpp_13_code import Counter
from 13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_case(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
        self.assertEqual(count_common(words), [('apple', 3), ('banana', 2), ('orange', 1)])

    def test_edge_case_single_word(self):
        words = ['apple']
        self.assertEqual(count_common(words), [('apple', 1)])

    def test_edge_case_no_common_words(self):
        words = ['apple', 'banana', 'orange', 'grape']
        self.assertEqual(count_common(words), [])

    def test_edge_case_more_than_four_words(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']
        self.assertEqual(count_common(words), [('apple', 4), ('banana', 2), ('orange', 1)])

    def test_corner_case_empty_list(self):
        words = []
        self.assertEqual(count_common(words), [])
