import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_simple_repeating_subseq(self):
        self.assertEqual(find_longest_repeating_subseq("ababc"), 3)
        self.assertEqual(find_longest_repeating_subseq("aabbbc"), 3)
        self.assertEqual(find_longest_repeating_subseq("ababab"), 2)

    def test_edge_cases(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)
        self.assertEqual(find_longest_repeating_subseq("a"), 1)
        self.assertEqual(find_longest_repeating_subseq("aa"), 1)
        self.assertEqual(find_longest_repeating_subseq("aaaa"), 1)
        self.assertEqual(find_longest_repeating_subseq("aabaa"), 2)

    def test_boundary_conditions(self):
        self.assertEqual(find_longest_repeating_subseq("a" * 1000), 1)
        self.assertEqual(find_longest_repeating_subseq("a" * 1000 + "b"), 1)
        self.assertEqual(find_longest_repeating_subseq("a" * 1000 + "aa"), 2)

    def test_complex_cases(self):
        self.assertEqual(find_longest_repeating_subseq("ababcdababcd"), 4)
        self.assertEqual(find_longest_repeating_subseq("ababcdababcdababcd"), 5)
        self.assertEqual(find_longest_repeating_subseq("ababcdababcdababcdababcd"), 6)
