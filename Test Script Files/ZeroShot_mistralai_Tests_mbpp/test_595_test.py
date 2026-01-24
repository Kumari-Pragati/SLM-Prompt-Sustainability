import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("aabbcc", "aabbcc"), 0)
        self.assertEqual(min_Swaps("", ""), 0)

    def test_min_swaps_identical_strings(self):
        self.assertEqual(min_Swaps("aaa", "aaa"), 0)
        self.assertEqual(min_Swaps("bbbb", "bbbb"), 0)
        self.assertEqual(min_Swaps("ccccc", "ccccc"), 0)

    def test_min_swaps_single_difference(self):
        self.assertEqual(min_Swaps("abcd", "acbd"), 1)
        self.assertEqual(min_Swaps("abcd", "adbc"), 1)
        self.assertEqual(min_Swaps("abcd", "acdb"), 1)

    def test_min_swaps_multiple_differences(self):
        self.assertEqual(min_Swaps("abcd", "cdab"), 2)
        self.assertEqual(min_Swaps("abcd", "dcba"), 3)
        self.assertEqual(min_Swaps("abcd", "dcba"), 2)

    def test_min_swaps_not_possible(self):
        self.assertEqual(min_Swaps("abcd", "acde"), "Not Possible")
        self.assertEqual(min_Swaps("abcd", "acdba"), "Not Possible")
        self.assertEqual(min_Swaps("abcd", "acdbz"), "Not Possible")
