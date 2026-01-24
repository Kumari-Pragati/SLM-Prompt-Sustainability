import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ["Hello world", "This is a test", "Remove words with 'is'"]
        charlist = ['is']
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello world", "This test", "Remove words with '"]

    def test_empty_list(self):
        list1 = []
        charlist = ['is']
        result = remove_words(list1, charlist)
        self.assertEqual(result, [])

    def test_empty_charlist(self):
        list1 = ["Hello world", "This is a test", "Remove words with 'is'"]
        charlist = []
        result = remove_words(list1, charlist)
        self.assertEqual(result, list1)

    def test_multiple_charlist(self):
        list1 = ["Hello world", "This is a test", "Remove words with 'is' and 'a'"]
        charlist = ['is', 'a']
        result = remove_words(list1, charlist)
        self.assertEqual(result, ["Hello world", "Remove words with '"])

    def test_non_string_input(self):
        list1 = [1, 2, 3]
        charlist = ['is']
        with self.assertRaises(TypeError):
            remove_words(list1, charlist)
