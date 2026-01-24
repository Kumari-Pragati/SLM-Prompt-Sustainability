import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_remove_words(self):
        list1 = ["Hello world", "Python is awesome", "I love coding"]
        charlist = ["world", "is", "love"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello", "Python awesome", "I coding"])

    def test_remove_words_empty_list(self):
        list1 = []
        charlist = ["world", "is", "love"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_remove_words_empty_charlist(self):
        list1 = ["Hello world", "Python is awesome", "I love coding"]
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, list1)

    def test_remove_words_no_matches(self):
        list1 = ["Hello world", "Python is awesome", "I love coding"]
        charlist = ["abc", "xyz", "def"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, list1)
