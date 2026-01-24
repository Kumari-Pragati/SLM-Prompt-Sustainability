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
        self.assertEqual(reverse_vowels("AEIOUaeiou"), "UOIEAuoiea")

    def test_edge_case4(self):
        self.assertEqual(reverse_vowels("123456"), "123456")

    def test_edge_case5(self):
        self.assertEqual(reverse_vowels("aAeEoO"), "oEeAa")

    def test_edge_case6(self):
        self.assertEqual(reverse_vowels("aAeEoO123"), "oEeAa123")

    def test_edge_case7(self):
        self.assertEqual(reverse_vowels("aAeEoO123456"), "oEeAa123456")

    def test_edge_case8(self):
        self.assertEqual(reverse_vowels("aAeEoO123456789"), "oEeAa123456789")

    def test_edge_case9(self):
        self.assertEqual(reverse_vowels("aAeEoO1234567890"), "oEeAa1234567890")

    def test_edge_case10(self):
        self.assertEqual(reverse_vowels("aAeEoO1234567890abcdef"), "oEeAa1234567890abcdef")
