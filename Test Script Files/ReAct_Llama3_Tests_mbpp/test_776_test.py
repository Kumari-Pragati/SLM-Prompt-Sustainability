import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_edge_case1(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_edge_case2(self):
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 5)

    def test_edge_case4(self):
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 0)

    def test_edge_case5(self):
        self.assertEqual(count_vowels("hello world"), 3)

    def test_edge_case6(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_edge_case7(self):
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZAEIOU"), 5)

    def test_edge_case8(self):
        self.assertEqual(count_vowels("AEIOUbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 5)

    def test_edge_case9(self):
        self.assertEqual(count_vowels("hello worldAEIOU"), 3)

    def test_edge_case10(self):
        self.assertEqual(count_vowels("AEIOUbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZhello world"), 5)
