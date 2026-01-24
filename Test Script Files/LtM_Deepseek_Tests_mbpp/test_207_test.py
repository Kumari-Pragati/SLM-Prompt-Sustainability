import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_longest_repeating_subseq("aab"), 1)
        self.assertEqual(find_longest_repeating_subseq("aabb"), 2)
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)
        self.assertEqual(find_longest_repeating_subseq("a"), 0)
        self.assertEqual(find_longest_repeating_subseq("aaaa"), 2)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(find_longest_repeating_subseq("aabbaab"), 3)
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 0)
        self.assertEqual(find_longest_repeating_subseq("aabbcc"), 0)
        self.assertEqual(find_longest_repeating_subseq("aabbaabb"), 2)
