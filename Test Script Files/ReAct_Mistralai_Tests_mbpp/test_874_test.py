import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_empty_strings(self):
        self.assertTrue(check_Concat("", ""))
        self.assertFalse(check_Concat("", "a"))
        self.assertFalse(check_Concat("a", ""))

    def test_single_character_strings(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(check_Concat(char, char))

    def test_different_lengths(self):
        self.assertFalse(check_Concat("abc", "def"))
        self.assertFalse(check_Concat("abc", "defg"))
        self.assertFalse(check_Concat("abc", "defgh"))

    def test_same_length_different_characters(self):
        self.assertFalse(check_Concat("aaa", "bbb"))
        self.assertFalse(check_Concat("aaa", "bbba"))
        self.assertFalse(check_Concat("aaa", "bbbba"))

    def test_longer_string_with_repeated_shorter_string(self):
        self.assertTrue(check_Concat("aaaaaa", "a"))
        self.assertTrue(check_Concat("aaaaaa", "aa"))
        self.assertTrue(check_Concat("aaaaaa", "aaa"))

    def test_error_handling(self):
        self.assertRaises(TypeError, check_Concat, 1, "str")
        self.assertRaises(TypeError, check_Concat, "str", 1)
