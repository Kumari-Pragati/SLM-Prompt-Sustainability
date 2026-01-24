import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_longest_repeating_subseq("aab"), 1)
        self.assertEqual(find_longest_repeating_subseq("aabb"), 2)
        self.assertEqual(find_longest_repeating_subseq("aabbaab"), 3)

    def test_edge_cases(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)
        self.assertEqual(find_longest_repeating_subseq("a"), 0)
        self.assertEqual(find_longest_repeating_subseq("aaa"), 1)

    def test_corner_cases(self):
        self.assertEqual(find_longest_repeating_subseq("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(find_longest_repeating_subseq("aabbccddeeffgghhiijjkkllmmnnoopp"), 2)
