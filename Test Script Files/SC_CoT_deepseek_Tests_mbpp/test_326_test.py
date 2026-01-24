import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_occurrences(['hello world', 'hello python']), 'hello')

    def test_single_word_case(self):
        self.assertEqual(most_occurrences(['python']), 'python')

    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), '')

    def test_all_same_words(self):
        self.assertEqual(most_occurrences(['same same', 'same same', 'same same']), 'same')

    def test_edge_case_with_whitespace(self):
        self.assertEqual(most_occurrences(['   ']), '')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(most_occurrences(['']), '')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(most_occurrences(['!@#$%^&*', '!@#$%^&*']), '!@#$%^&*')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            most_occurrences(123)
