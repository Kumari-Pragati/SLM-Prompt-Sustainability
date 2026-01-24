import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_occurrences(['hello world', 'hello python']), 'hello')

    def test_edge_case_single_word(self):
        self.assertEqual(most_occurrences(['hello']), 'hello')

    def test_boundary_case_empty_list(self):
        self.assertEqual(most_occurrences([]), '')

    def test_corner_case_repeated_words(self):
        self.assertEqual(most_occurrences(['hello hello', 'world world']), 'hello')

    def test_corner_case_mixed_case(self):
        self.assertEqual(most_occurrences(['Hello hello', 'World world']), 'Hello')

    def test_corner_case_special_characters(self):
        self.assertEqual(most_occurrences(['hello! world', 'hello world']), 'hello')
