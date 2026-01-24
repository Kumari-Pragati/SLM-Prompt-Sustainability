import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_simple_equal_strings(self):
        self.assertEqual(min_Swaps("aa", "aa"), 0)
        self.assertEqual(min_Swaps("ab", "ab"), 0)

    def test_simple_different_strings(self):
        self.assertEqual(min_Swaps("aa", "bb"), 2)
        self.assertEqual(min_Swaps("ab", "ac"), 1)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps("", "a"), 1)
        self.assertEqual(min_Swaps("a", ""), 1)
        self.assertEqual(min_Swaps("aa", "a"), 1)
        self.assertEqual(min_Swaps("a", "aa"), 1)

    def test_boundary_cases(self):
        self.assertEqual(min_Swaps("a" * 1000001, "a" * 1000000), 1000000)
        self.assertEqual(min_Swaps("a" * 1000001, "a" * 1000001), "Not Possible")

    def test_complex_cases(self):
        self.assertEqual(min_Swaps("abab", "baab"), 1)
        self.assertEqual(min_Swaps("abab", "abba"), "Not Possible")
