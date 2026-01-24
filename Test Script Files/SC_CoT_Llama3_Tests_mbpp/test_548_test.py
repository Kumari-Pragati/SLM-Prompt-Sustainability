import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), 5)

    def test_edge_case(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 2, 3, 4]), 4)

    def test_edge_case2(self):
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    def test_edge_case3(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 4, 3, 2, 1]), 5)

    def test_edge_case4(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_edge_case5(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 1, 1, 1]), 1)

    def test_edge_case6(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]), 5)

    def test_edge_case7(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1]), 5)

    def test_edge_case8(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1]), 5)

    def test_edge_case9(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1]), 5)

    def test_edge_case10(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1]), 5)

    def test_edge_case11(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]), 5)

    def test_edge_case12(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]), 5)

    def test_edge_case13(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]), 5)

    def test_edge_case14(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 5)

    def test_edge_case15(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 5)

    def test_edge_case16(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 5)
