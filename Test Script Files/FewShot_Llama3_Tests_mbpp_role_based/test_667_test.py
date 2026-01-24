import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_empty_vowels(self):
        self.assertEqual(Check_Vow("hello", ""), 0)

    def test_no_vowels(self):
        self.assertEqual(Check_Vow("bcd", "aeiou"), 0)

    def test_multiple_vowels(self):
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            Check_Vow(123, "aeiou")

    def test_non_string_vowels_input(self):
        with self.assertRaises(TypeError):
            Check_Vow("hello", 123)
