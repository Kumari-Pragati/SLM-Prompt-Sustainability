import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words_typical(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), ['apple'])

    def test_remove_words_edge(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_remove_words_empty_list(self):
        list1 = []
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_remove_words_empty_removewords(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        self.assertEqual(remove_words(list1, removewords), ['apple', 'banana', 'cherry'])

    def test_remove_words_no_match(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['grape', 'orange']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'banana', 'cherry'])

    def test_remove_words_multiple_matches(self):
        list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        removewords = ['banana', 'cherry', 'date']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'elderberry'])
