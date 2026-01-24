import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_edge_case_empty_vowels(self):
        self.assertEqual(Check_Vow("hello", ""), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(Check_Vow("a", "aeiou"), 1)

    def test_edge_case_single_char_not_vowel(self):
        self.assertEqual(Check_Vow("b", "aeiou"), 0)

    def test_edge_case_multiple_vowels(self):
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)

    def test_edge_case_multiple_chars(self):
        self.assertEqual(Check_Vow("hello world", "aeiou"), 3)

    def test_edge_case_multiple_chars_and_spaces(self):
        self.assertEqual(Check_Vow("hello world", "aeiou"), 3)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            Check_Vow(123, "aeiou")

    def test_edge_case_non_string_input_vowels(self):
        with self.assertRaises(TypeError):
            Check_Vow("hello", 123)
