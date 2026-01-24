import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_remove_single_word(self):
        input_list = ['apple', 'banana', 'cherry']
        remove_words = ['apple']
        expected_output = ['banana', 'cherry']
        self.assertEqual(remove_words(input_list, remove_words), expected_output)

    def test_remove_multiple_words(self):
        input_list = ['apple', 'banana', 'cherry', 'apple', 'orange']
        remove_words = ['apple', 'banana']
        expected_output = ['cherry', 'orange']
        self.assertEqual(remove_words(input_list, remove_words), expected_output)

    def test_empty_list(self):
        input_list = []
        remove_words = ['apple']
        self.assertEqual(remove_words(input_list, remove_words), [])

    def test_empty_remove_words(self):
        input_list = ['apple', 'banana', 'cherry']
        remove_words = []
        self.assertEqual(remove_words(input_list, remove_words), input_list)

    def test_word_not_in_list(self):
        input_list = ['apple', 'banana', 'cherry']
        remove_words = ['orange']
        self.assertEqual(remove_words(input_list, remove_words), input_list)

    def test_word_not_in_list1(self):
        input_list = ['apple', 'banana', 'cherry']
        remove_words = ['apple', 'orange']
        self.assertEqual(remove_words(input_list, remove_words), ['banana', 'cherry'])
