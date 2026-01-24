import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_simple(self):
        list1 = [1, 2, 3, 4, 5]
        removewords = [2, 4]
        result = remove_words(list1, removewords)
        self.assertEqual(result, [1, 3, 5])

    def test_empty_list(self):
        list1 = []
        removewords = [1, 2, 3]
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_empty_removewords(self):
        list1 = [1, 2, 3, 4, 5]
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_no_words_to_remove(self):
        list1 = [1, 2, 3, 4, 5]
        removewords = []
        result = remove_words(list1, removewords)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_remove_all_words(self):
        list1 = [1, 2, 3, 4, 5]
        removewords = [1, 2, 3, 4, 5]
        result = remove_words(list1, removewords)
        self.assertEqual(result, [])

    def test_remove_some_words(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        removewords = [2, 4, 6, 8]
        result = remove_words(list1, removewords)
        self.assertEqual(result, [1, 3, 5, 7, 9, 10])
