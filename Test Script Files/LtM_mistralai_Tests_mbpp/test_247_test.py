import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(lps("abab"), 2)

    def test_edge_case_short(self):
        self.assertEqual(lps("a"), 1)

    def test_edge_case_long(self):
        self.assertEqual(lps("a" * 100), 1)

    def test_palindrome(self):
        self.assertEqual(lps("radar"), 4)

    def test_different_chars(self):
        self.assertEqual(lps("abcd"), 1)

    def test_complex_case(self):
        self.assertEqual(lps("ababcdabab"), 5)

    def test_invalid_input(self):
        self.assertRaises(TypeError, lps, 123)
