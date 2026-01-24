import unittest
from mbpp_13_code import Counter
from 13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_input(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
        self.assertListEqual(count_common(words), [('apple', 3), ('banana', 2), ('orange', 1)])

    def test_edge_cases_1(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'apple']
        self.assertListEqual(count_common(words), [('apple', 4), ('banana', 2), ('orange', 1)])

    def test_edge_cases_2(self):
        words = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple', 'orange', 'apple', 'banana']
        self.assertListEqual(count_common(words), [('apple', 5), ('banana', 2), ('orange', 1)])

    def test_edge_cases_3(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'orange', 'apple', 'banana', 'apple']
        self.assertListEqual(count_common(words), [('apple', 6), ('banana', 2), ('orange', 1)])

    def test_empty_list(self):
        self.assertListEqual(count_common([]), [])

    def test_single_word(self):
        words = ['apple']
        self.assertListEqual(count_common(words), [('apple', 1)])

    def test_multiple_single_words(self):
        words = ['apple', 'banana', 'orange']
        self.assertListEqual(count_common(words), [('apple', 1), ('banana', 1), ('orange', 1)])

    def test_special_case(self):
        words = ['a', 'aa', 'aaa', 'aaaa']
        self.assertListEqual(count_common(words), [('a', 1), ('aa', 2), ('aaa', 1), ('aaaa', 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_common(123)
