import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("Hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("HELLO", "AEIOU"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_edge_case_single_vowel(self):
        self.assertEqual(Check_Vow("a", "aeiou"), 1)
        self.assertEqual(Check_Vow("A", "AEIOU"), 1)

    def test_edge_case_no_vowels(self):
        self.assertEqual(Check_Vow("spam", "aeiou"), 0)

    def test_edge_case_vowels_in_uppercase(self):
        self.assertEqual(Check_Vow("AEIOU", "aeiou"), 5)

    def test_edge_case_vowels_in_mixed_case(self):
        self.assertEqual(Check_Vow("AeIoU", "aeiou"), 4)

    def test_edge_case_invalid_vowels(self):
        self.assertEqual(Check_Vow("hello", "xyz"), 0)
