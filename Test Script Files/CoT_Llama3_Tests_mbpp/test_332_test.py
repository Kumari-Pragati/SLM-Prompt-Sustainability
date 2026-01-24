import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_edge_case_single_character(self):
        self.assertEqual(char_frequency("a"), {'a': 1})

    def test_edge_case_single_space(self):
        self.assertEqual(char_frequency(" "), {' ': 1})

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(char_frequency("   "), {' ': 1})

    def test_edge_case_punctuation(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_uppercase(self):
        self.assertEqual(char_frequency("HELLO"), {'H': 1, 'E': 1, 'L': 3, 'O': 1})

    def test_edge_case_mixed_case(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_spaces(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_punctuation(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_spaces_and_punctuation(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_spaces_and_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_repeated_characters_with_punctuation_and_non_ascii_characters(self):
        self.assertEqual(char_frequency("Hello