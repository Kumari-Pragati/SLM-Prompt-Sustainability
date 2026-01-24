import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("aabb"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("aabba"), 2)
