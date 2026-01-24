import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aab"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 2)

    def test_corner_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("abcba"), 5)
