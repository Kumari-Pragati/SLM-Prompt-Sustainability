import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_simple_even_length(self):
        self.assertEqual(remove_odd("abcdef"), "abcd")

    def test_simple_odd_length(self):
        self.assertEqual(remove_odd("abcde"), "abcd")

    def test_edge_empty_string(self):
        self.assertEqual(remove_odd(""), "")

    def test_edge_single_character(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_edge_max_length(self):
        self.assertEqual(remove_odd("a" * 1000), "a" * 998)

    def test_edge_min_length(self):
        self.assertEqual(remove_odd("a" * 2), "a")

    def test_complex_mixed_odd_even(self):
        self.assertEqual(remove_odd("abcdefg"), "abcdg")

    def test_complex_repeated_characters(self):
        self.assertEqual(remove_odd("aaabbbccc"), "aabbcc")
