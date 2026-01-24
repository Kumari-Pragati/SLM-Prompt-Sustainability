import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words(self):
        list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        removewords = ['banana', 'date']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'cherry', 'elderberry'])

    def test_remove_words_empty_list(self):
        list1 = []
        removewords = ['banana', 'date']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_remove_words_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date', 'elderberry'])

    def test_remove_words_multiple_occurrences(self):
        list1 = ['apple', 'banana', 'banana', 'cherry', 'date', 'elderberry']
        removewords = ['banana', 'date']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'cherry', 'elderberry'])
