import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_same_characters(self):
        self.assertEqual(Repeat("aaabbb"), ["a", "b"])

    def test_single_character(self):
        self.assertEqual(Repeat("a"), ["a"])

    def test_empty_string(self):
        self.assertEqual(Repeat(""), [])

    def test_different_characters(self):
        self.assertEqual(Repeat("abcdefg"), [])

    def test_duplicate_characters_at_boundary(self):
        self.assertEqual(Repeat("aa"), ["a"])

    def test_duplicate_characters_in_middle(self):
        self.assertEqual(Repeat("abba"), ["a", "b"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Repeat(123)
