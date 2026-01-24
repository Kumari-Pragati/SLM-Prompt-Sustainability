import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), "Equal")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(check_Equality(char), "Equal")

    def test_multiple_characters_strings(self):
        for str1 in ["aa", "ab", "ba", "bb"]:
            for str2 in ["aa", "ab", "ba", "bb"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))

    def test_mixed_case_strings(self):
        for str1 in ["Aa", "Ab", "Ba", "Bb"]:
            for str2 in ["Aa", "Ab", "Ba", "Bb"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))

    def test_strings_with_numbers(self):
        for str1 in ["a1", "a2", "a3", "1a", "2a", "3a"]:
            for str2 in ["a1", "a2", "a3", "1a", "2a", "3a"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))

    def test_strings_with_special_characters(self):
        for str1 in ["a!", "a@", "a#", "!a", "@a", "#a"]:
            for str2 in ["a!", "a@", "a#", "!a", "@a", "#a"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))

    def test_strings_with_multiple_special_characters(self):
        for str1 in ["!@a", "!@b", "@!a", "@!b"]:
            for str2 in ["!@a", "!@b", "@!a", "@!b"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))

    def test_strings_with_numbers_and_special_characters(self):
        for str1 in ["a!1", "a@2", "a#3", "!a1", "@a2", "#a3"]:
            for str2 in ["a!1", "a@2", "a#3", "!a1", "@a2", "#a3"]:
                self.assertEqual(check_Equality(str1), check_Equality(str2))
