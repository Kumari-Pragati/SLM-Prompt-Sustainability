import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_input(self):
        list1 = ['apple', 'banana', 'orange']
        removewords = ['banana', 'orange']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_edge_case_empty_list(self):
        list1 = []
        removewords = ['banana', 'orange']
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_edge_case_empty_removewords(self):
        list1 = ['apple', 'banana', 'orange']
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, list1)

    def test_edge_case_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'orange']
        removewords = ['grape', 'pear']
        result = remove_words(list1, removewords)
        self.assertEqual(result, list1)

    def test_edge_case_duplicates(self):
        list1 = ['apple', 'banana', 'banana', 'orange']
        removewords = ['banana', 'orange']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_edge_case_duplicates_to_remove(self):
        list1 = ['apple', 'banana', 'banana', 'orange']
        removewords = ['banana', 'banana', 'orange']
        result = remove_words(list1, removewords)
        self.assertEqual(result, ['apple'])

    def test_invalid_input_non_list(self):
        list1 = 'apple'
        removewords = ['banana', 'orange']
        with self.assertRaises(TypeError):
            remove_words(list1, removewords)

    def test_invalid_input_non_list2(self):
        list1 = ['apple']
        removewords = 'banana'
        with self.assertRaises(TypeError):
            remove_words(list1, removewords)
