import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_vowels("hello"), 0)

    def test_edge_case1(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_edge_case2(self):
        self.assertEqual(count_vowels("aeioua"), 6)

    def test_edge_case3(self):
        self.assertEqual(count_vowels("aeiouaeiou"), 10)

    def test_edge_case4(self):
        self.assertEqual(count_vowels("aeiouaeioua"), 11)

    def test_edge_case5(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiou"), 15)

    def test_edge_case6(self):
        self.assertEqual(count_vowels("aeiouaeiouaeioua"), 16)

    def test_edge_case7(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiou"), 20)

    def test_edge_case8(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeioua"), 21)

    def test_edge_case9(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiou"), 25)

    def test_edge_case10(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeioua"), 26)

    def test_edge_case11(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiou"), 30)

    def test_edge_case12(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeioua"), 31)

    def test_edge_case13(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 35)

    def test_edge_case14(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 36)

    def test_edge_case15(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 40)

    def test_edge_case16(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 41)

    def test_edge_case17(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 45)

    def test_edge_case18(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 46)

    def test_edge_case19(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 50)

    def test_edge_case20(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 51)

    def test_edge_case21(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 55)

    def test_edge_case22(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 56)

    def test_edge_case23(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 60)

    def test_edge_case24(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 61)

    def test_edge_case25(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 65)

    def test_edge_case26(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeioua"), 66)

    def test_edge_case27(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 70)

    def test_edge_case28(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou