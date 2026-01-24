import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_vowels("hello"), 0)

    def test_edge_case_start(self):
        self.assertEqual(count_vowels("aeiou"), 0)

    def test_edge_case_end(self):
        self.assertEqual(count_vowels("iuoa"), 0)

    def test_edge_case_middle(self):
        self.assertEqual(count_vowels("aieo"), 0)

    def test_edge_case_start_end(self):
        self.assertEqual(count_vowels("aeiou"), 0)

    def test_edge_case_start_end_middle(self):
        self.assertEqual(count_vowels("aieou"), 0)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count_vowels("a"), 0)

    def test_edge_case_single_character_non_vowel(self):
        self.assertEqual(count_vowels("b"), 0)
