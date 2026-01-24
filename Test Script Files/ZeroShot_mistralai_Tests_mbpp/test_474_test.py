import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_replace_char_with_single_character(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLo")
        self.assertEqual(replace_char("World", "r", "R"), "WoLd")
        self.assertEqual(replace_char("Python", "h", "H"), "PytHon")

    def test_replace_char_with_multiple_occurrences(self):
        self.assertEqual(replace_char("aaabbb", "a", "A"), "AAbbbb")
        self.assertEqual(replace_char("Mississippi", "s", "S"), "MisMissippi")
        self.assertEqual(replace_char("HelloWorld", "l", "L"), "HeLloWrLd")

    def test_replace_char_with_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")
        self.assertEqual(replace_char("abc", "", "x"), "abc")
        self.assertEqual(replace_char("ab", "b", ""), "a")
