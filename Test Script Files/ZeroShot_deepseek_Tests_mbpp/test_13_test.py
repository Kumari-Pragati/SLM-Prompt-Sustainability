import unittest
from mbpp_13_code import Counter
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_count_common(self):
        words = ['apple', 'orange', 'banana', 'apple', 'orange', 'banana', 'apple', 'mango']
        expected_output = [('apple', 3), ('orange', 2), ('banana', 2), ('mango', 1)]
        self.assertEqual(count_common(words), expected_output)

    def test_count_common_empty_list(self):
        words = []
        expected_output = []
        self.assertEqual(count_common(words), expected_output)

    def test_count_common_single_word(self):
        words = ['apple']
        expected_output = [('apple', 1)]
        self.assertEqual(count_common(words), expected_output)

    def test_count_common_same_words(self):
        words = ['apple', 'apple', 'apple', 'apple']
        expected_output = [('apple', 4)]
        self.assertEqual(count_common(words), expected_output)
