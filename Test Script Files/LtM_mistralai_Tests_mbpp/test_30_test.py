import unittest
from mbpp_30_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_Substring_WithEqualEnds("abba"), 1)

    def test_empty_string(self):
        self.assertEqual(count_Substring_WithEqualEnds(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_WithEqualEnds("a"), 0)

    def test_odd_length(self):
        self.assertEqual(count_Substring_WithEqualEnds("abc"), 0)

    def test_palindrome(self):
        self.assertEqual(count_Substring_WithEqualEnds("racecar"), 5)

    def test_edge_case_min(self):
        self.assertEqual(count_Substring_WithEqualEnds("a" * 1000), 1000)

    def test_edge_case_max(self):
        self.assertEqual(count_Substring_WithEqualEnds("a" * 100000), 100000)
