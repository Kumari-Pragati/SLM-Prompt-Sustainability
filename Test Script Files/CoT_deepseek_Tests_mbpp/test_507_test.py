import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['apple', 'banana', 'cherry', 'banana']
        removewords = ['banana']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'cherry'])

    def test_empty_list(self):
        list1 = []
        removewords = ['apple']
        self.assertEqual(remove_words(list1, removewords), [])

    def test_no_match(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['mango']
        self.assertEqual(remove_words(list1, removewords), ['apple', 'banana', 'cherry'])

    def test_duplicates_in_removewords(self):
        list1 = ['apple', 'banana', 'banana']
        removewords = ['banana', 'banana']
        self.assertEqual(remove_words(list1, removewords), ['apple'])

    def test_case_sensitivity(self):
        list1 = ['Apple', 'banana', 'Banana']
        removewords = ['banana']
        self.assertEqual(remove_words(list1, removewords), ['Apple', 'Banana'])

    def test_remove_all(self):
        list1 = ['apple', 'banana', 'cherry']
        removewords = ['apple', 'banana', 'cherry']
        self.assertEqual(remove_words(list1, removewords), [])
