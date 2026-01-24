import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_edge_case1(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_edge_case2(self):
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 5)

    def test_edge_case4(self):
        self.assertEqual(count_vowels("AEIOU"), 0)

    def test_edge_case5(self):
        self.assertEqual(count_vowels("aeiouAEIOUbcd"), 5)

    def test_edge_case6(self):
        self.assertEqual(count_vowels("AEIOUbcd"), 0)

    def test_edge_case7(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOU"), 5)

    def test_edge_case8(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcd"), 5)

    def test_edge_case9(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case10(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case11(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case12(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case13(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case14(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case15(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case16(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case17(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case18(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case19(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd"), 5)

    def test_edge_case20(self):
        self.assertEqual(count_vowels("AEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcdAEIOUbcd