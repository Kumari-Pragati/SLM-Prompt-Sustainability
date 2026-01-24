import unittest
from546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(last_occurence_char("", "a"))

    def test_single_char(self):
        self.assertEqual(last_occurence_char("a", "a"), 1)
        self.assertIsNone(last_occurence_char("A", "a"))

    def test_multiple_chars(self):
        self.assertEqual(last_occurence_char("abcabc", "c"), 5)
        self.assertEqual(last_occurence_char("abcabc", "a"), 0)
        self.assertIsNone(last_occurence_char("abcabc", "z"))

    def test_multiple_occurrences(self):
        self.assertEqual(last_occurence_char("aaabbc", "a"), 4)
        self.assertEqual(last_occurence_char("aaabbc", "b"), 3)
