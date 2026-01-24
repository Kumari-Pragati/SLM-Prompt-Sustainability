import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "banana"]), "banana")
        self.assertEqual(most_occurrences(["hello", "world", "hello", "world", "world", "world"]), "world")

    def test_edge_case_single_word(self):
        self.assertEqual(most_occurrences(["apple"]), "apple")
        self.assertEqual(most_occurrences(["hello"]), "hello")

    def test_edge_case_empty_list(self):
        self.assertEqual(most_occurrences([]), None)

    def test_edge_case_single_word_list_with_numbers(self):
        self.assertEqual(most_occurrences(["1", "apple"]), None)
        self.assertEqual(most_occurrences(["apple", "1"]), None)
        self.assertEqual(most_occurrences(["1", "apple", "1"]), "1")

    def test_corner_case_different_occurrences(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "orange", "banana"]), "banana")
