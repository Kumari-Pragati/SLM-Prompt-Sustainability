import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_case(self):
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']
        expected = [('cherry', 3), ('banana', 2), ('apple', 2)]
        self.assertEqual(count_common(words), expected)

    def test_edge_case_single_word(self):
        words = ['apple']
        expected = [('apple', 1)]
        self.assertEqual(count_common(words), expected)

    def test_edge_case_empty_list(self):
        words = []
        expected = []
        self.assertEqual(count_common(words), expected)

    def test_boundary_case_four_different_words(self):
        words = ['apple', 'banana', 'cherry', 'date']
        expected = [('apple', 1), ('banana', 1), ('cherry', 1), ('date', 1)]
        self.assertEqual(count_common(words), expected)

    def test_boundary_case_four_same_words(self):
        words = ['apple', 'apple', 'apple', 'apple']
        expected = [('apple', 4)]
        self.assertEqual(count_common(words), expected)

    def test_corner_case_repeated_words(self):
        words = ['apple', 'apple', 'apple', 'apple', 'banana', 'banana']
        expected = [('apple', 4), ('banana', 2)]
        self.assertEqual(count_common(words), expected)
