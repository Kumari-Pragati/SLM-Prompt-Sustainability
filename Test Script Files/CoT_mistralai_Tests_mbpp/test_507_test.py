import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_words([], ["apple", "banana"]), [])

    def test_no_match(self):
        self.assertListEqual(remove_words(["apple", "banana"], ["orange", "grape"]), ["apple", "banana"])

    def test_single_match(self):
        self.assertListEqual(remove_words(["apple", "banana"], ["apple"]), ["banana"])

    def test_multiple_matches(self):
        self.assertListEqual(remove_words(["apple", "banana", "apple"], ["apple"]), ["banana"])

    def test_case_sensitivity(self):
        self.assertListEqual(remove_words(["Apple", "Banana"], ["apple"]), ["Banana"])

    def test_remove_all(self):
        self.assertListEqual(remove_words(["apple", "apple", "banana", "apple"], ["apple"]), ["banana"])

    def test_remove_none(self):
        self.assertListEqual(remove_words(["apple", "banana"], ["orange"]), ["apple", "banana"])

    def test_empty_removewords(self):
        self.assertListEqual(remove_words(["apple", "banana"], []), ["apple", "banana"])

    def test_list_with_only_removewords(self):
        self.assertListEqual(remove_words(["apple"], ["apple"]), [])

    def test_invalid_input_type_list1(self):
        with self.assertRaises(TypeError):
            remove_words(1, ["apple"])

    def test_invalid_input_type_removewords(self):
        with self.assertRaises(TypeError):
            remove_words(["apple"], 1)
