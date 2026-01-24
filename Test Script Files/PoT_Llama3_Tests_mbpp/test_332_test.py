import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(char_frequency("Hello World"), {'H': 1, 'e': 1, 'l': 3, 'o': 2,'': 1, 'W': 1, 'r': 1, 'd': 1})

    def test_edge_case_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_edge_case_single_character(self):
        self.assertEqual(char_frequency("a"), {'a': 1})

    def test_edge_case_single_space(self):
        self.assertEqual(char_frequency(" "), {' ': 1})

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(char_frequency("   "), {' ': 1})

    def test_edge_case_multiple_characters(self):
        self.assertEqual(char_frequency("abc"), {'a': 1, 'b': 1, 'c': 1})

    def test_edge_case_multiple_characters_with_duplicates(self):
        self.assertEqual(char_frequency("aaabbbcc"), {'a': 3, 'b': 3, 'c': 3})

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1,'': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1})

    def test_edge_case_non_ascii_characters_with_duplicates(self):
        self.assertEqual(char_frequency("Hello, World!!"), {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1,'': 1, 'W': 1, 'r': 1, 'd': 1, '!': 2})
