import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ["hello world", "Python is awesome"]
        charlist = ["world", "awesome"]
        expected_output = ["hello", "Python is"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_empty_list(self):
        list1 = []
        charlist = ["world", "awesome"]
        expected_output = []
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_empty_charlist(self):
        list1 = ["hello world", "Python is awesome"]
        charlist = []
        expected_output = ["hello world", "Python is awesome"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_all_words_removed(self):
        list1 = ["hello world", "Python is awesome"]
        charlist = ["hello", "world", "Python", "is", "awesome"]
        expected_output = [""] * len(list1)
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_case_sensitivity(self):
        list1 = ["Hello world", "Python is Awesome"]
        charlist = ["world", "awesome"]
        expected_output = ["Hello", "Python is"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_whitespace_handling(self):
        list1 = [" hello world ", " Python is awesome "]
        charlist = ["world", "awesome"]
        expected_output = ["hello", "Python is"]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_invalid_input(self):
        list1 = ["hello world", "Python is awesome"]
        charlist = ["world", 123]
        with self.assertRaises(TypeError):
            remove_words(list1, charlist)
