import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ["Hello world", "Python is awesome", "This is a test"]
        charlist = ["world", "is"]
        self.assertEqual(remove_words(list1, charlist), ["Hello", "Python awesome", "This a test"])

    def test_edge_case_empty_list(self):
        list1 = []
        charlist = ["world", "is"]
        self.assertEqual(remove_words(list1, charlist), [])

    def test_edge_case_empty_charlist(self):
        list1 = ["Hello world", "Python is awesome", "This is a test"]
        charlist = []
        self.assertEqual(remove_words(list1, charlist), list1)

    def test_edge_case_single_word(self):
        list1 = ["Hello"]
        charlist = ["world", "is"]
        self.assertEqual(remove_words(list1, charlist), ["Hello"])

    def test_edge_case_single_word_in_charlist(self):
        list1 = ["Hello"]
        charlist = ["Hello", "is"]
        self.assertEqual(remove_words(list1, charlist), [])

    def test_edge_case_multiple_words(self):
        list1 = ["Hello world", "Python is awesome", "This is a test"]
        charlist = ["world", "is", "a"]
        self.assertEqual(remove_words(list1, charlist), ["Hello", "Python awesome", "This test"])

    def test_edge_case_multiple_words_in_charlist(self):
        list1 = ["Hello world", "Python is awesome", "This is a test"]
        charlist = ["world", "is", "a", "test"]
        self.assertEqual(remove_words(list1, charlist), [])
