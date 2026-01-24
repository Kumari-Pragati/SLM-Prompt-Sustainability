import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", set("aeiou")), 0)

    def test_single_vowel(self):
        self.assertEqual(Check_Vow("a", set("aeiou")), 1)

    def test_multiple_vowels(self):
        self.assertEqual(Check_Vow("aeiou", set("aeiou")), 5)

    def test_mixed_case_vowels(self):
        self.assertEqual(Check_Vow("AeIoU", set("aeiou")), 5)

    def test_non_vowel_string(self):
        self.assertEqual(Check_Vow("xyz", set("aeiou")), 0)

    def test_vowel_set_with_non_vowels(self):
        with self.assertRaises(ValueError):
            Check_Vow("aeiou", set("xyz"))

    def test_vowel_set_with_empty_set(self):
        with self.assertRaises(ValueError):
            Check_Vow("aeiou", set())
