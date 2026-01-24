import unittest
from mbpp_247_code import lps

class TestLps(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character_string(self):
        self.assertEqual(lps("a"), 1)

    def test_two_character_string(self):
        self.assertEqual(lps("aa"), 2)

    def test_three_character_string(self):
        self.assertEqual(lps("aba"), 3)

    def test_four_character_string(self):
        self.assertEqual(lps("abba"), 4)

    def test_five_character_string(self):
        self.assertEqual(lps("ababa"), 5)

    def test_long_string(self):
        self.assertEqual(lps("abababa"), 6)

    def test_non_matching_characters(self):
        self.assertEqual(lps("abc"), 1)

    def test_non_matching_characters_long(self):
        self.assertEqual(lps("abcabc"), 2)

    def test_repeated_characters(self):
        self.assertEqual(lps("aaaa"), 4)

    def test_repeated_characters_long(self):
        self.assertEqual(lps("aaaaaa"), 6)
