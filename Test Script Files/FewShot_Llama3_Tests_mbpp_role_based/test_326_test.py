import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [["hello", "world", "hello"], ["python", "is", "awesome"]]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(most_occurrences(test_list), "")

    def test_edge_case_single_element_list(self):
        test_list = [["hello"]]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_single_word_list(self):
        test_list = [["hello", "hello", "hello"]]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_multiple_occurrences(self):
        test_list = [["hello", "world", "hello", "world", "hello"]]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_edge_case_no_occurrences(self):
        test_list = [["apple", "banana", "orange"]]
        self.assertEqual(most_occurrences(test_list), "")
