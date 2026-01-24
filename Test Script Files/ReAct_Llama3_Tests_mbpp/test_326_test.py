import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), '')

    def test_single_word(self):
        self.assertEqual(most_occurrences([['hello']]), 'hello')

    def test_multiple_words(self):
        self.assertEqual(most_occurrences([['hello', 'world']]), 'hello')

    def test_multiple_words_with_duplicates(self):
        self.assertEqual(most_occurrences([['hello', 'world', 'hello']]), 'hello')

    def test_multiple_sublists(self):
        self.assertEqual(most_occurrences([['hello', 'world'], ['hello', 'python']]), 'hello')

    def test_multiple_sublists_with_duplicates(self):
        self.assertEqual(most_occurrences([['hello', 'world', 'hello'], ['hello', 'python']]), 'hello')

    def test_empty_sublist(self):
        self.assertEqual(most_occurrences([['', 'world']]), 'world')

    def test_all_empty_sublist(self):
        self.assertEqual(most_occurrences([['', '']]), '')
