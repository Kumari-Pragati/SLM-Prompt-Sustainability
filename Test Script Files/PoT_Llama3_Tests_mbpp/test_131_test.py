import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_edge_case(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_edge_case2(self):
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")

    def test_edge_case3(self):
        self.assertEqual(reverse_vowels("123456"), "123456")

    def test_edge_case4(self):
        self.assertEqual(reverse_vowels("abcdef"), "efcba")

    def test_edge_case5(self):
        self.assertEqual(reverse_vowels("AEIOU123"), "UOIEA321")

    def test_edge_case6(self):
        self.assertEqual(reverse_vowels("hello world"), "holle dlrow")

    def test_edge_case7(self):
        self.assertEqual(reverse_vowels("AEIOU world"), "UOIEA dlrow")

    def test_edge_case8(self):
        self.assertEqual(reverse_vowels("hello123 world"), "holle dlrow321")

    def test_edge_case9(self):
        self.assertEqual(reverse_vowels("AEIOU123 world"), "UOIEA dlrow321")
