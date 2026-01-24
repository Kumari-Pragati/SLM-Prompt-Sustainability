import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(lps(char), 1)

    def test_palindrome(self):
        self.assertEqual(lps("racecar"), 6)
        self.assertEqual(lps("level"), 5)
        self.assertEqual(lps("madam"), 4)

    def test_longer_palindrome(self):
        self.assertEqual(lps("radarlevel"), 8)
        self.assertEqual(lps("radarlevelradar"), 16)

    def test_non_palindrome(self):
        self.assertEqual(lps("hello"), 2)
        self.assertEqual(lps("programming"), 3)
        self.assertEqual(lps("python"), 2)

    def test_edge_cases(self):
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)
        self.assertEqual(lps("ab"), 1)
        self.assertEqual(lps("aab"), 2)
        self.assertEqual(lps("aabb"), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lps(123)
        with self.assertRaises(TypeError):
            lps(None)
        with self.assertRaises(TypeError):
            lps([])
