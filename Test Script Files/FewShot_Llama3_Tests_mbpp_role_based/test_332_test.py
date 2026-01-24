import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_edge_case_single_character_string(self):
        self.assertEqual(char_frequency("a"), {'a': 1})

    def test_edge_case_single_space_string(self):
        self.assertEqual(char_frequency(" "), {' ': 1})

    def test_edge_case_multiple_spaces_string(self):
        self.assertEqual(char_frequency("   "), {' ': 3})

    def test_edge_case_non_ascii_characters_string(self):
        self.assertEqual(char_frequency("Hello, World! à"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1, '!': 1, 'à': 1})
