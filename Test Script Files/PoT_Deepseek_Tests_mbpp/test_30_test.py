import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcab"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("aabbaa"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("aaaa"), 6)

    def test_edge_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_corner_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("abcba"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("abcdcba"), 4)
