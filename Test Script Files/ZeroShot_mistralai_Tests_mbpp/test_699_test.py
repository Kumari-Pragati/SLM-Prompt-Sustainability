import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("aabbcc", "aabbcc"), 0)
        self.assertEqual(min_Swaps("", ""), 0)

    def test_min_swaps_identical_swaps(self):
        self.assertEqual(min_Swaps("aabbcc", "ccbaabaa"), 3)
        self.assertEqual(min_Swaps("aabbcc", "ccbaabaa"), 3)

    def test_min_swaps_single_swap(self):
        self.assertEqual(min_Swaps("aabbcc", "abcbac"), 1)
        self.assertEqual(min_Swaps("abcbac", "aabbcc"), 1)

    def test_min_swaps_multiple_swaps(self):
        self.assertEqual(min_Swaps("aabbcc", "bcaabb"), 2)
        self.assertEqual(min_Swaps("bcaabb", "aabbcc"), 2)

    def test_min_swaps_not_possible(self):
        self.assertEqual(min_Swaps("aabbcc", "abcbad"), "Not Possible")
        self.assertEqual(min_Swaps("abcbad", "aabbcc"), "Not Possible")
