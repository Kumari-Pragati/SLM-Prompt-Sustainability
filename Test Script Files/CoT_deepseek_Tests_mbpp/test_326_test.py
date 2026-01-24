import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_typical_case(self):
        test_list = ["hello world", "world hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_single_word(self):
        test_list = ["hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_empty_list(self):
        test_list = []
        self.assertEqual(most_occurrences(test_list), "")

    def test_same_occurrences(self):
        test_list = ["hello world", "world hello", "hello world"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_with_spaces(self):
        test_list = ["  hello  world  ", "world hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_with_numbers(self):
        test_list = ["123 456", "456 123"]
        self.assertEqual(most_occurrences(test_list), "123")

    def test_edge_case_with_special_characters(self):
        test_list = ["!@# $%%^", "$%%^ !@#"]
        self.assertEqual(most_occurrences(test_list), "!@#")
