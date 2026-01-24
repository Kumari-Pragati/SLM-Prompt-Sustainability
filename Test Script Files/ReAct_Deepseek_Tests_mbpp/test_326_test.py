import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_typical_case(self):
        test_list = ["hello world", "world hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_single_word_list(self):
        test_list = ["hello", "world"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(most_occurrences(test_list))

    def test_same_occurrence_words(self):
        test_list = ["hello world", "world hello", "hello world"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_all_same_words(self):
        test_list = ["hello hello hello", "world world world"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_empty_strings(self):
        test_list = ["", ""]
        self.assertIsNone(most_occurrences(test_list))

    def test_whitespace_only_strings(self):
        test_list = [" ", " "]
        self.assertIsNone(most_occurrences(test_list))

    def test_mixed_case_words(self):
        test_list = ["Hello world", "World hello"]
        self.assertEqual(most_occurrences(test_list), "Hello")
