import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), ['apple'])

    def test_edge_case_empty_list(self):
        list1 = []
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_edge_case_empty_removewords(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        self.assertEqual(remove_words(list1, removewords), list1)

    def test_edge_case_list1_empty_removewords(self):
        list1 = []
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_edge_case_removewords_empty_list1(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        self.assertEqual(remove_words(list1, removewords), list1)

    def test_typical_case_multiple_words(self):
        list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        removewords = ['banana', 'cherry', 'date']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'elderberry'])

    def test_typical_case_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        self.assertEqual(remove_words(list1, removewords), list1)

    def test_typical_case_all_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])
