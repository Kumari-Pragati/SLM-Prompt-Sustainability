import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_case(self):
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']
        expected = [('cherry', 3), ('banana', 2), ('apple', 2)]
        self.assertEqual(count_common(words), expected)

    def test_single_word(self):
        words = ['apple']
        expected = [('apple', 1)]
        self.assertEqual(count_common(words), expected)

    def test_empty_list(self):
        words = []
        expected = []
        self.assertEqual(count_common(words), expected)

    def test_top_four_words(self):
        words = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'date', 'apple']
        expected = [('apple', 3), ('banana', 2), ('cherry', 2), ('date', 2)]
        self.assertEqual(count_common(words), expected)

    def test_same_frequency_words(self):
        words = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'apple', 'banana']
        expected = [('apple', 3), ('banana', 3), ('cherry', 2), ('date', 1)]
        self.assertEqual(count_common(words), expected)

    def test_invalid_input(self):
        words = 12345
        with self.assertRaises(TypeError):
            count_common(words)
