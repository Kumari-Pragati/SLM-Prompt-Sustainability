import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(remove_words([], []), [])

    def test_no_matching_words(self):
        self.assertListEqual(remove_words(["Hello", "World", "Python"], ["o", "d"]), ["Hello", "World", "Python"])

    def test_matching_words(self):
        self.assertListEqual(remove_words(["apple", "banana", "apple pie"], ["apple", "pie"]), ["banana"])

    def test_multiple_lists(self):
        self.assertListEqual(remove_words([["apple", "banana"], ["apple pie", "orange juice"]], ["apple", "pie"]),
                             [["banana"], ["orange juice"]])

    def test_case_insensitive(self):
        self.assertListEqual(remove_words(["Apple", "Banana", "Apple Pie"], ["apple", "pie"]), ["Banana"])
