import unittest
from mbpp_332_code import char_frequency

class TestCharFrequency(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(char_frequency("Hello, World!"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 2, 'l': 1, 'd': 1, '!': 1})

    def test_edge_case_empty_string(self):
        self.assertEqual(char_frequency(""), {})

    def test_edge_case_single_char(self):
        self.assertEqual(char_frequency("a"), {'a': 1})

    def test_edge_case_single_space(self):
        self.assertEqual(char_frequency(" "), {' ': 1})

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(char_frequency("   "), {' ': 1})

    def test_edge_case_punctuation(self):
        self.assertEqual(char_frequency(".,!"), {',': 1, '.': 1, '!': 1})

    def test_edge_case_multiple_punctuation(self):
        self.assertEqual(char_frequency(".,!!"), {',': 1, '.': 1, '!': 2})

    def test_edge_case_multiple_chars(self):
        self.assertEqual(char_frequency("abcabc"), {'a': 2, 'b': 2, 'c': 2})

    def test_edge_case_repeating_chars(self):
        self.assertEqual(char_frequency("aaa"), {'a': 3})

    def test_edge_case_repeating_spaces(self):
        self.assertEqual(char_frequency("   "), {' ': 1})

    def test_edge_case_repeating_punctuation(self):
        self.assertEqual(char_frequency("!!!!"), {'!': 4})

    def test_edge_case_mixed_chars(self):
        self.assertEqual(char_frequency("Hello, World! abc"), {'H': 1, 'e': 1, 'l': 3, ',': 1,'': 1, 'W': 1, 'o': 1, 'r': 2, 'l': 1, 'd': 1, '!': 1, 'a': 1, 'b': 1, 'c': 1})

    def test_edge_case_mixed_punctuation(self):
        self.assertEqual(char_frequency(".,!!abc"), {',': 1, '.': 1, '!': 2, 'a': 1, 'b': 1, 'c': 1})

    def test_edge_case_mixed_spaces(self):
        self.assertEqual(char_frequency("   abc"), {' ': 1, 'a': 1, 'b': 1, 'c': 1})

    def test_edge_case_mixed_chars_and_spaces(self):
        self.assertEqual(char_frequency("   abc,!!"), {' ': 1, 'a': 1, 'b': 1, 'c': 1, ',': 1, '.': 1, '!': 2})

    def test_edge_case_mixed_chars_and_punctuation(self):
        self.assertEqual(char_frequency("abc,!!"), {'a': 1, 'b': 1, 'c': 1, ',': 1, '.': 1, '!': 2})

    def test_edge_case_mixed_chars_spaces_and_punctuation(self):
        self.assertEqual(char_frequency("abc,!!   "), {'a': 1, 'b': 1, 'c': 1, ',': 1, '.': 1, '!': 2,'': 1})
