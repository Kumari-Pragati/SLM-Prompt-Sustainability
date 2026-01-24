import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_simple_input(self):
        self.assertListEqual(find_long_word("This is a simple test"), ["simple"])

    def test_multiple_words(self):
        self.assertListEqual(find_long_word("Longer words are easier to find"), ["easier", "Longer"])

    def test_edge_case_min_length(self):
        self.assertListEqual(find_long_word("a"), [])

    def test_edge_case_max_length(self):
        self.assertListEqual(find_long_word("This is a very very very very very very very very very long word"), ["very", "long"])

    def test_case_sensitivity(self):
        self.assertListEqual(find_long_word("This Is A Test"), ["This", "A"])

    def test_special_characters(self):
        self.assertListEqual(find_long_word("123LongWord456"), ["LongWord"])

    def test_punctuation(self):
        self.assertListEqual(find_long_word("Hello, World! This is a test."), ["World"])

    def test_multiple_word_lengths(self):
        self.assertListEqual(find_long_word("ShortWordLongWordShort"), ["LongWord"])
