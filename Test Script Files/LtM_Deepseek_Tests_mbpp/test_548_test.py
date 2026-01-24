import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(longest_increasing_subsequence([5, 8, 7, 1, 6]), 3)
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)
        self.assertEqual(longest_increasing_subsequence([1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), 5)
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(longest_increasing_subsequence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
