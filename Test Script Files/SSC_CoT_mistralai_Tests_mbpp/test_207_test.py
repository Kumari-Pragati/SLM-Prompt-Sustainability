import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_longest_repeating_subseq("bananabannana"), 3)
        self.assertEqual(find_longest_repeating_subseq("abcabcabc"), 3)
        self.assertEqual(find_longest_repeating_subseq("abababab"), 1)
        self.assertEqual(find_longest_repeating_subseq("a"), 1)
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_longest_repeating_subseq("aabb"), 2)
        self.assertEqual(find_longest_repeating_subseq("aaab"), 2)
        self.assertEqual(find_longest_repeating_subseq("abba"), 2)
        self.assertEqual(find_longest_repeating_subseq("abab"), 2)
        self.assertEqual(find_longest_repeating_subseq("bananana"), 3)
        self.assertEqual(find_longest_repeating_subseq("banananabana"), 3)
        self.assertEqual(find_longest_repeating_subseq("banananabanaa"), 4)
