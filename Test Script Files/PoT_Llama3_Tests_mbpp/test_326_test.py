import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(most_occurrences([["hello", "world", "hello"]]), "hello")

    def test_edge_case_empty_list(self):
        self.assertEqual(most_occurrences([]), "")

    def test_edge_case_single_word(self):
        self.assertEqual(most_occurrences([["hello"]]), "hello")

    def test_edge_case_multiple_words(self):
        self.assertEqual(most_occurrences([["hello", "world", "hello", "world"]]), "hello")

    def test_edge_case_duplicates(self):
        self.assertEqual(most_occurrences([["hello", "hello", "world", "world"]]), "hello")

    def test_edge_case_no_duplicates(self):
        self.assertEqual(most_occurrences([["hello", "world"]]), "hello")

    def test_edge_case_empty_sublist(self):
        self.assertEqual(most_occurrences([["", "world"]]), "world")

    def test_edge_case_single_sublist(self):
        self.assertEqual(most_occurrences([["hello"]]), "hello")

    def test_edge_case_multiple_sublists(self):
        self.assertEqual(most_occurrences([["hello", "world", "hello", "world"]]), "hello")

    def test_edge_case_duplicates_sublists(self):
        self.assertEqual(most_occurrences([["hello", "hello", "world", "world"]]), "hello")

    def test_edge_case_no_duplicates_sublists(self):
        self.assertEqual(most_occurrences([["hello", "world"]]), "hello")
