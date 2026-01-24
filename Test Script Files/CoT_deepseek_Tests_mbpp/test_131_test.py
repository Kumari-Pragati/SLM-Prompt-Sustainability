import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_case_with_capital_vowels(self):
        self.assertEqual(reverse_vowels("HELLO"), "HOLLE")

    def test_case_with_mixed_case(self):
        self.assertEqual(reverse_vowels("HeLlO"), "HoLlE")

    def test_case_with_no_vowels(self):
        self.assertEqual(reverse_vowels("rhythm"), "rhythm")

    def test_case_with_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_case_with_special_characters(self):
        self.assertEqual(reverse_vowels("h@e#l*l"), "h@e#l*l")

    def test_case_with_numbers(self):
        self.assertEqual(reverse_vowels("h3ll4"), "h3ll4")

    def test_case_with_special_vowels(self):
        self.assertEqual(reverse_vowels("h€ll0"), "h€ll0")
