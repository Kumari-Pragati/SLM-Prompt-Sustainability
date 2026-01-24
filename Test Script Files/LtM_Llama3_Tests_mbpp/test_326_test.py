import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(most_occurrences(["hello", "world"]), "hello")

    def test_empty_input(self):
        self.assertEqual(most_occurrences([]), "")

    def test_single_word(self):
        self.assertEqual(most_occurrences(["hello"]), "hello")

    def test_multiple_words(self):
        self.assertEqual(most_occurrences(["hello", "world", "hello"]), "hello")

    def test_empty_sublist(self):
        self.assertEqual(most_occurrences([["", ""]]), "")

    def test_multiple_sublists(self):
        self.assertEqual(most_occurrences([["hello", "world"], ["hello", "foo"]]), "hello")

    def test_empty_sublist_with_word(self):
        self.assertEqual(most_occurrences([["hello", "world"], [""]]), "hello")

    def test_multiple_sublists_with_word(self):
        self.assertEqual(most_occurrences([["hello", "world"], ["hello", "foo"], ["hello", "bar"]]), "hello")
