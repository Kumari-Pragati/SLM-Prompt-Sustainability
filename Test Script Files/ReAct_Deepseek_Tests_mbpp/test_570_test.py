import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ["Hello world", "Python is great"]
        charlist = ["world"]
        expected_output = ["Hello ", "Python is great"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_edge_case_empty_list(self):
        list1 = []
        charlist = ["world"]
        expected_output = []
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_edge_case_empty_charlist(self):
        list1 = ["Hello world", "Python is great"]
        charlist = []
        expected_output = ["Hello world", "Python is great"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_edge_case_all_words_in_charlist(self):
        list1 = ["Hello world", "Python is great"]
        charlist = ["Hello", "world", "Python", "is", "great"]
        expected_output = ["", ""]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            remove_words(None, ["world"])

    def test_error_case_non_list_input(self):
        with self.assertRaises(TypeError):
            remove_words("Hello world", ["world"])

    def test_error_case_non_string_in_list(self):
        with self.assertRaises(TypeError):
            remove_words(["Hello world", 123], ["world"])
