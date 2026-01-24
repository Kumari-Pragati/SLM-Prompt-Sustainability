import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_consecutive_strings(self):
        self.assertTrue(check_Concat("abc", "abc"))

    def test_longer_string_is_multiple_of_shorter(self):
        self.assertTrue(check_Concat("abcd", "ab"))

    def test_shorter_string_is_multiple_of_longer(self):
        self.assertTrue(check_Concat("ab", "abcd"))

    def test_empty_strings(self):
        self.assertTrue(check_Concat("", ""))

    def test_single_character_strings(self):
        self.assertTrue(check_Concat("a", "a"))

    def test_different_strings(self):
        self.assertFalse(check_Concat("abc", "xyz"))

    def test_mismatched_characters(self):
        self.assertFalse(check_Concat("abcd", "abce"))
