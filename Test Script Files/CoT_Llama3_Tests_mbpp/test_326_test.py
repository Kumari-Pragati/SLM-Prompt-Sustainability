import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(most_occurrences([["hello", "world"], ["hello", "again"]]), "hello")

    def test_edge_case_empty_list(self):
        self.assertEqual(most_occurrences([]), "")

    def test_edge_case_single_word(self):
        self.assertEqual(most_occurrences([["hello"]]), "hello")

    def test_edge_case_single_word_multiple_lists(self):
        self.assertEqual(most_occurrences([["hello"], ["hello"], ["world"]]), "hello")

    def test_edge_case_multiple_words(self):
        self.assertEqual(most_occurrences([["hello", "world", "hello"], ["world", "again"]]), "hello")

    def test_edge_case_multiple_words_multiple_lists(self):
        self.assertEqual(most_occurrences([["hello", "world", "hello"], ["world", "again"], ["hello", "again"]]), "hello")

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            most_occurrences("hello")

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            most_occurrences([1, 2, 3])
