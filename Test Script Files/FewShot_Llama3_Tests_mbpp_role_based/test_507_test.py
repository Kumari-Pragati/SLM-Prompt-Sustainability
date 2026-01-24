import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_remove_single_word(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'cherry'])

    def test_remove_multiple_words(self):
        list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        removewords = ['banana', 'date']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'cherry', 'elderberry'])

    def test_remove_all_words(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_remove_no_words(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'banana', 'cherry'])

    def test_remove_words_with_duplicates(self):
        list1 = ['apple', 'banana', 'banana', 'cherry']
        removewords = ['banana']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'cherry'])
