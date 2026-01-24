import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Check_Vow("", ["a", "e", "i", "o", "u"]), 0)

    def test_single_vowel(self):
        self.assertEqual(Check_Vow("a", ["a", "e", "i", "o", "u"]), 1)

    def test_multiple_vowels(self):
        self.assertEqual(Check_Vow("aeiou", ["a", "e", "i", "o", "u"]), 5)

    def test_mixed_case_vowels(self):
        self.assertEqual(Check_Vow("AeIoU", ["a", "e", "i", "o", "u"]), 4)

    def test_non_vowel_string(self):
        self.assertEqual(Check_Vow("xyz", ["a", "e", "i", "o", "u"]), 0)

    def test_vowel_not_in_list(self):
        self.assertEqual(Check_Vow("a", ["b", "c", "d", "e", "f"]), 0)

    def test_string_with_digits(self):
        self.assertEqual(Check_Vow("a1b2c3", ["a", "e", "i", "o", "u"]), 1)

    def test_string_with_special_characters(self):
        self.assertEqual(Check_Vow("a!b@c#", ["a", "e", "i", "o", "u"]), 1)
