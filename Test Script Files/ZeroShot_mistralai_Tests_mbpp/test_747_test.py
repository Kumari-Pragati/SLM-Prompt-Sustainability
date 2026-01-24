import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(lcs_of_three("", "", ""), 0)

    def test_single_char_strings(self):
        self.assertEqual(lcs_of_three("a", "b", "a"), 1)
        self.assertEqual(lcs_of_three("a", "b", "c"), 0)

    def test_simple_strings(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "ab"), 2)
        self.assertEqual(lcs_of_three("abc", "acd", "ab"), 1)
        self.assertEqual(lcs_of_three("abc", "bcd", "ab"), 0)

    def test_complex_strings(self):
        self.assertEqual(lcs_of_three("banana", "apple", "monkey"), 1)
        self.assertEqual(lcs_of_three("banana", "app", "monkey"), 0)
        self.assertEqual(lcs_of_three("banana", "banan", "monkey"), 3)
