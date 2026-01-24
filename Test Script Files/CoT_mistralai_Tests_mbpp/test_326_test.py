import unittest
from mbpp_326_code import defaultdict
from thirty_two_six import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), '')

    def test_single_element(self):
        self.assertEqual(most_occurrences(['word']), 'word')

    def test_multiple_elements_single_word(self):
        self.assertEqual(most_occurrences(['word', 'word', 'word']), 'word')

    def test_multiple_elements_different_words(self):
        self.assertEqual(most_occurrences(['word1', 'word2', 'word1', 'word2', 'word1']), 'word1')

    def test_case_sensitivity(self):
        self.assertEqual(most_occurrences(['Word', 'word', 'word']), 'word')

    def test_multiple_occurrences_same_word(self):
        self.assertEqual(most_occurrences(['word', 'word', 'word', 'other', 'other', 'word']), 'word')

    def test_edge_case_long_strings(self):
        self.assertEqual(most_occurrences(['longstringlongstringlongstring']), 'longstring')

    def test_edge_case_empty_words(self):
        self.assertEqual(most_occurrences(['', ' ', '  ']), '')

    def test_edge_case_no_words(self):
        self.assertEqual(most_occurrences([]), '')

    def test_edge_case_single_space(self):
        self.assertEqual(most_occurrences([' ']), ' ')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            most_occurrences([1, 2, 3])
