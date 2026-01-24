import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_empty_list(self):
        list1 = []
        removewords = ['apple']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, list1)

    def test_all_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_duplicate_words(self):
        list1 = ['apple', 'banana', 'apple']
        removewords = ['apple']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['banana'])

    def test_case_sensitivity(self):
        list1 = ['Apple', 'banana', 'Cherry']
        removewords = ['apple', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['banana'])
