import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), ['apple'])

    def test_empty_list(self):
        list1 = []
        removewords = ['apple']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_no_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = []
        self.assertEqual(remove_words(list1, removewords), ['apple', 'banana', 'cherry'])

    def test_all_words_to_remove(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_duplicate_words_in_list(self):
        list1 = ['apple', 'banana', 'apple']
        removewords = ['apple']
        self.assertEqual(remove_words(list1, removewords), ['banana'])

    def test_case_sensitivity(self):
        list1 = ['apple', 'Banana', 'cherry']
        removewords = ['banana']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'cherry'])
