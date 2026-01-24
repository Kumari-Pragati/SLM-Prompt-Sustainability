import unittest
from mbpp_30_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_SubstringWithEqualEnds(""), 0)

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(count_SubstringWithEqualEnds(char), 1)

    def test_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds("racecar"), 5)

    def test_non_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds("hello"), 0)

    def test_case_sensitivity(self):
        self.assertEqual(count_SubstringWithEqualEnds("RaceCar"), 5)
        self.assertEqual(count_SubstringWithEqualEnds("racecar"), 5)

    def test_long_string(self):
        self.assertEqual(count_SubstringWithEqualEnds("zebraZebra"), 2)

    def test_edge_cases(self):
        self.assertEqual(count_SubstringWithEqualEnds(""), 0)
        self.assertEqual(count_SubstringWithEqualEnds("a"), 1)
        self.assertEqual(count_SubstringWithEqualEnds("aa"), 1)
        self.assertEqual(count_SubstringWithEqualEnds("ab"), 0)
        self.assertEqual(count_SubstringWithEqualEnds("aba"), 1)
        self.assertEqual(count_SubstringWithEqualEnds("abab"), 2)
