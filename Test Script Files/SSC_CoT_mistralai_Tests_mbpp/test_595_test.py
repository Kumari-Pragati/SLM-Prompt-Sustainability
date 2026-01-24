import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(min_Swaps("abcd", "dcba"), 2)
        self.assertEqual(min_Swaps("aabb", "bbaa"), 1)
        self.assertEqual(min_Swaps("aa", "aa"), 0)
        self.assertEqual(min_Swaps("abcd", "acbd"), 2)

    def test_edge_case_1(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("aaa", "aaa"), 0)

    def test_edge_case_2(self):
        self.assertEqual(min_Swaps("abc", "cba"), "Not Possible")
        self.assertEqual(min_Swaps("abcd", "ac"), "Not Possible")
        self.assertEqual(min_Swaps("abcd", "abcdx"), "Not Possible")

    def test_invalid_input(self):
        self.assertRaises(TypeError, min_Swaps, 1, 2)
        self.assertRaises(TypeError, min_Swaps, "a", 1)
