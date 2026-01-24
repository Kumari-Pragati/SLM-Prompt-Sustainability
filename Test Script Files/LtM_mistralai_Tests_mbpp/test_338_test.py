import unittest
from338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 1)

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_odd_length(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_palindrome(self):
        self.assertEqual(count_Substring_With_Equal_Ends("racecar"), 6)

    def test_edge_case_min(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a" * 1000), 1000)

    def test_edge_case_max(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a" * 100000), 100000)
