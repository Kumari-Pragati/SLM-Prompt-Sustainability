import unittest
from684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count_Char("a", "a"), 1)
        self.assertEqual(count_Char("A", "a"), 0)

    def test_multiple_characters(self):
        self.assertEqual(count_Char("aaa", "a"), 3)
        self.assertEqual(count_Char("AAA", "a"), 3)
        self.assertEqual(count_Char("aaA", "a"), 2)

    def test_longer_string(self):
        self.assertEqual(count_Char("abcdefghijklmnopqrstuvwxyz", "a"), 1)
        self.assertEqual(count_Char("abcdefghijklmnopqrstuvwxyz", "z"), 1)

    def test_string_with_repetitions(self):
        self.assertEqual(count_Char("aaaaaa", "a"), 6)

    def test_string_with_partial_match(self):
        self.assertEqual(count_Char("abcabc", "a"), 3)
        self.assertEqual(count_Char("abcabc", "b"), 2)
        self.assertEqual(count_Char("abcabc", "c"), 1)
