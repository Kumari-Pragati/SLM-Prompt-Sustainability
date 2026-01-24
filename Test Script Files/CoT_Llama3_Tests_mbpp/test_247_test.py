import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_lps_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_lps_single_char(self):
        self.assertEqual(lps("a"), 1)

    def test_lps_two_chars(self):
        self.assertEqual(lps("aa"), 2)

    def test_lps_three_chars(self):
        self.assertEqual(lps("aba"), 3)

    def test_lps_four_chars(self):
        self.assertEqual(lps("abba"), 4)

    def test_lps_five_chars(self):
        self.assertEqual(lps("ababa"), 5)

    def test_lps_non_matching(self):
        self.assertEqual(lps("abc"), 1)

    def test_lps_long_string(self):
        self.assertEqual(lps("abababab"), 6)

    def test_lps_long_non_matching(self):
        self.assertEqual(lps("abcdefg"), 1)
