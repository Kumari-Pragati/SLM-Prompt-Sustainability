import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_typical_input(self):
        list1 = ["Hello world", "Python is awesome", "Code is fun"]
        charlist = ["world", "is", "fun"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello", "Python awesome", "Code is"])

    def test_edge_case_empty_input(self):
        list1 = []
        charlist = ["world", "is", "fun"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_edge_case_empty_charlist(self):
        list1 = ["Hello world", "Python is awesome", "Code is fun"]
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, list1)

    def test_edge_case_single_word(self):
        list1 = ["Hello"]
        charlist = ["world", "is", "fun"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello"])

    def test_edge_case_single_char(self):
        list1 = ["Hello world"]
        charlist = ["w"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello  "])

    def test_edge_case_multiple_words(self):
        list1 = ["Hello world", "Python is awesome", "Code is fun"]
        charlist = ["world", "is", "fun", "Code"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello", "Python awesome"])

    def test_edge_case_multiple_chars(self):
        list1 = ["Hello world", "Python is awesome", "Code is fun"]
        charlist = ["world", "is", "fun", "Code", "Python"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_edge_case_empty_charlist_and_input(self):
        list1 = ["Hello world"]
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello world"])

    def test_edge_case_empty_input_and_charlist(self):
        list1 = []
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_edge_case_single_word_and_char(self):
        list1 = ["Hello"]
        charlist = ["Hello"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_edge_case_multiple_words_and_chars(self):
        list1 = ["Hello world", "Python is awesome", "Code is fun"]
        charlist = ["world", "is", "fun", "Code", "Python", "Hello"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])
