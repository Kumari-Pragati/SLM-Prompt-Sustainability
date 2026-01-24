import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(min_Swaps("abcd", "dcba"), 1)
        self.assertEqual(min_Swaps("aabb", "bbaa"), 1)
        self.assertEqual(min_Swaps("abc", "acb"), 1)

    def test_edge_case_even(self):
        self.assertEqual(min_Swaps("abcd", "cdab"), 2)
        self.assertEqual(min_Swaps("aabb", "baab"), 2)
        self.assertEqual(min_Swaps("abc", "cba"), 2)

    def test_edge_case_odd(self):
        self.assertEqual(min_Swaps("abcd", "dcba"), "Not Possible")
        self.assertEqual(min_Swaps("aabb", "bbaa"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "acb"), "Not Possible")

    def test_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("", "a"), "Not Possible")
        self.assertEqual(min_Swaps("a", ""), "Not Possible")

    def test_single_char_strings(self):
        self.assertEqual(min_Swaps("a", "a"), 0)
        self.assertEqual(min_Swaps("a", "b"), "Not Possible")

    def test_invalid_input(self):
        self.assertRaises(TypeError, min_Swaps, 1, 2)
        self.assertRaises(TypeError, min_Swaps, "1", 2)
        self.assertRaises(TypeError, min_Swaps, 1, "2")
