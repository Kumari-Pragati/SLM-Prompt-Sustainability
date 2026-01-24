import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("abcba"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("a" * 1000), 1000)

    def test_special_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("aabb"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(None)
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)
