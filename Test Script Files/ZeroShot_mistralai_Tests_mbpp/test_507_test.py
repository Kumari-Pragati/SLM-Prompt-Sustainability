import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_words([], ["apple", "banana"]), [])

    def test_single_word(self):
        self.assertListEqual(remove_words(["apple"], ["apple"]), [])
        self.assertListEqual(remove_words(["banana"], ["apple"]), ["banana"])

    def test_multiple_words(self):
        self.assertListEqual(remove_words(["apple", "banana", "apple", "orange", "apple"], ["apple"]), ["banana", "orange"])
        self.assertListEqual(remove_words(["apple", "banana", "orange", "apple"], ["banana", "orange"]), ["apple"])

    def test_case_insensitive(self):
        self.assertListEqual(remove_words(["Apple", "Banana", "Apple", "Orange", "Apple"], ["apple"]), ["Banana", "Orange"])

    def test_non_existent_word(self):
        self.assertListEqual(remove_words(["apple", "banana", "orange"], ["grape"]), ["apple", "banana", "orange"])
