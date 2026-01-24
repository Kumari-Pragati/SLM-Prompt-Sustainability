import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(find_long_word("This is a long word"), ["long"])

    def test_edge_case_shortest_5(self):
        self.assertListEqual(find_long_word("abcde"), ["abcde"])

    def test_edge_case_longest_5(self):
        self.assertListEqual(find_long_word("abcdefghij"), ["abcdef"])

    def test_edge_case_trailing_space(self):
        self.assertListEqual(find_long_word("This is a long word "), ["long"])

    def test_edge_case_leading_space(self):
        self.assertListEqual(find_long_word(" long word"), ["long"])

    def test_edge_case_multiple_words(self):
        self.assertListEqual(find_long_word("This is a long long word"), ["long", "long"])

    def test_edge_case_single_char(self):
        self.assertListEqual(find_long_word("a"), [])
