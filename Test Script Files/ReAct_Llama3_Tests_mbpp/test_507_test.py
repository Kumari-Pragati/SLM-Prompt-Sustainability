import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words_typical_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_remove_words_edge_case_empty_list(self):
        list1 = []
        removewords = ['banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_remove_words_edge_case_empty_removewords(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'banana', 'cherry'])

    def test_remove_words_edge_case_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['grape', 'orange']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple', 'banana', 'cherry'])

    def test_remove_words_edge_case_duplicates(self):
        list1 = ['apple', 'banana', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_remove_words_error_case_non_list_input(self):
        list1 = 'apple'
        removewords = ['banana', 'cherry']
        with self.assertRaises(TypeError):
            remove_words(list1, removewords)

    def test_remove_words_error_case_non_list_removewords(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = 'banana'
        with self.assertRaises(TypeError):
            remove_words(list1, removewords)
