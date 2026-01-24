import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_longest_repeating_subseq("ababcba"), 5)
        self.assertEqual(find_longest_repeating_subseq("ababab"), 3)
        self.assertEqual(find_longest_repeating_subseq("a"), 1)
        self.assertEqual(find_longest_repeating_subseq("aa"), 1)
        self.assertEqual(find_longest_repeating_subseq("aaaa"), 1)

    def test_edge_case(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)
        self.assertEqual(find_longest_repeating_subseq("a "), 1)
        self.assertEqual(find_longest_repeating_subseq(" a"), 1)
        self.assertEqual(find_longest_repeating_subseq("ab "), 1)
        self.assertEqual(find_longest_repeating_subseq(" ba"), 1)

    def test_corner_case(self):
        self.assertEqual(find_longest_repeating_subseq("abab"), 2)
        self.assertEqual(find_longest_repeating_subseq("ababab"), 3)
        self.assertEqual(find_longest_repeating_subseq("abababab"), 4)
        self.assertEqual(find_longest_repeating_subseq("ababababab"), 5)
