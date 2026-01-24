import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_typical_case(self):
        list1 = ["Hello world", "Python is fun", "This is a test"]
        charlist = ["world", "is"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello", "Python fun", "This a test"])

    def test_edge_case_empty_list(self):
        list1 = []
        charlist = ["world", "is"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_edge_case_empty_charlist(self):
        list1 = ["Hello world", "Python is fun", "This is a test"]
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, list1)

    def test_edge_case_single_word(self):
        list1 = ["Hello"]
        charlist = ["world", "is"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello"])

    def test_edge_case_single_word_in_charlist(self):
        list1 = ["Hello world", "is fun"]
        charlist = ["world", "is"]
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello", "fun"])

    def test_error_case_non_list_input(self):
        list1 = "Hello"
        charlist = ["world", "is"]
        with self.assertRaises(TypeError):
            remove_words(list1, charlist)

    def test_error_case_non_charlist_input(self):
        list1 = ["Hello", "world"]
        charlist = 123
        with self.assertRaises(TypeError):
            remove_words(list1, charlist)
