import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_empty_strings(self):
        self.assertTrue(check_Concat("", ""))

    def test_one_character_strings(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                self.assertTrue(check_Concat(char, char2))

    def test_different_lengths(self):
        self.assertFalse(check_Concat("abc", "def"))

    def test_different_characters(self):
        self.assertFalse(check_Concat("abcd", "efgh"))

    def test_same_length_different_characters(self):
        self.assertFalse(check_Concat("abcd", "1234"))

    def test_longer_string_with_prefix(self):
        self.assertTrue(check_Concat("abcdef", "abc"))

    def test_longer_string_with_suffix(self):
        self.assertTrue(check_Concat("abcdef", "def"))

    def test_longer_string_with_middle(self):
        self.assertTrue(check_Concat("abcdef", "adc"))
