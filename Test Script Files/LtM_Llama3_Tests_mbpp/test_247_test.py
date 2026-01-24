import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character(self):
        self.assertEqual(lps("a"), 1)

    def test_two_characters(self):
        self.assertEqual(lps("aa"), 2)

    def test_three_characters(self):
        self.assertEqual(lps("aba"), 3)

    def test_four_characters(self):
        self.assertEqual(lps("abba"), 4)

    def test_five_characters(self):
        self.assertEqual(lps("ababa"), 5)

    def test_edge_case(self):
        self.assertEqual(lps("abcba"), 4)

    def test_long_string(self):
        self.assertEqual(lps("abababab"), 6)

    def test_non_matching(self):
        self.assertEqual(lps("abc"), 1)

    def test_non_matching_long(self):
        self.assertEqual(lps("abcde"), 1)
