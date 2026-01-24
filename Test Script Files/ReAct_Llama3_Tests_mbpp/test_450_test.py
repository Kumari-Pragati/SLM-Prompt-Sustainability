import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(extract_string("", 3), [])

    def test_single_char_string(self):
        self.assertEqual(extract_string("a", 1), ["a"])

    def test_multiple_chars_string(self):
        self.assertEqual(extract_string("abc", 1), ["a", "b", "c"])

    def test_string_with_no_chars_of_length_l(self):
        self.assertEqual(extract_string("abc", 4), [])

    def test_string_with_chars_of_length_l(self):
        self.assertEqual(extract_string("abcd", 1), ["a", "b", "c", "d"])

    def test_string_with_chars_of_length_l_and_others(self):
        self.assertEqual(extract_string("abcde", 1), ["a", "b", "c", "d", "e"])

    def test_string_with_no_chars_of_length_l_and_others(self):
        self.assertEqual(extract_string("abcde", 2), [])
