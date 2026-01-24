import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("world", "aeiou"), 2)
        self.assertEqual(Check_Vow("python", "aeiou"), 2)

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_empty_vowels(self):
        self.assertEqual(Check_Vow("hello", ""), 0)

    def test_single_vowel(self):
        self.assertEqual(Check_Vow("hello", "o"), 1)
        self.assertEqual(Check_Vow("world", "o"), 1)

    def test_multiple_vowels(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("world", "aeiou"), 2)

    def test_non_vowel(self):
        self.assertEqual(Check_Vow("hello", "xyz"), 0)

    def test_mixed_case(self):
        self.assertEqual(Check_Vow("Hello", "aeiou"), 1)
        self.assertEqual(Check_Vow("WORLD", "aeiou"), 1)
