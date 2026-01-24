import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_last_occurence_single_char(self):
        self.assertEqual(last_occurence_char("abcabc", "c"), 5)

    def test_last_occurence_multiple_chars(self):
        self.assertEqual(last_occurence_char("abccabc", "c"), 6)

    def test_last_occurence_empty_string(self):
        self.assertIsNone(last_occurence_char("", "a"))

    def test_last_occurence_no_char(self):
        self.assertIsNone(last_occurence_char("abc", "z"))

    def test_last_occurence_negative_index(self):
        self.assertIsNone(last_occurence_char("abc", "-1"))
