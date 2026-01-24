import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(last_occurence_char("", "a"))

    def test_single_char_string(self):
        self.assertEqual(last_occurence_char("a", "a"), 1)
        self.assertIsNone(last_occurence_char("A", "a"))

    def test_multiple_chars_string(self):
        self.assertEqual(last_occurence_char("abcabc", "c"), 5)
        self.assertEqual(last_occurence_char("abcabc", "a"), 0)
        self.assertIsNone(last_occurence_char("abcabc", "d"))

    def test_boundary_cases(self):
        self.assertEqual(last_occurence_char("a" * 1000, "a"), 1000)
        self.assertEqual(last_occurence_char("a" * 1000 + "a", "a"), 1001)
