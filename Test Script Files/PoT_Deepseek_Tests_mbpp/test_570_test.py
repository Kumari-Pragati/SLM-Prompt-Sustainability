import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ["hello world", "this is a test"]
        charlist = ["world", "test"]
        self.assertEqual(remove_words(list1, charlist), ["hello  ", "this is a  "])

    def test_edge_case_empty_list(self):
        list1 = []
        charlist = ["test"]
        self.assertEqual(remove_words(list1, charlist), [])

    def test_boundary_case_single_word(self):
        list1 = ["hello"]
        charlist = ["hello"]
        self.assertEqual(remove_words(list1, charlist), ["  "])

    def test_corner_case_no_match(self):
        list1 = ["hello world", "this is a test"]
        charlist = ["nonexistent"]
        self.assertEqual(remove_words(list1, charlist), ["hello world", "this is a test"])

    def test_corner_case_all_words_removed(self):
        list1 = ["hello world", "this is a test"]
        charlist = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(remove_words(list1, charlist), ["  ", "  "])
