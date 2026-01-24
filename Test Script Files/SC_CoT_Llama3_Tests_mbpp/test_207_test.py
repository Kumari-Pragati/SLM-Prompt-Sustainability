import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 3)

    def test_edge_case(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_edge_case2(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_edge_case3(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_edge_case4(self):
        self.assertEqual(find_longest_repeating_subseq("aba"), 2)

    def test_edge_case5(self):
        self.assertEqual(find_longest_repeating_subseq("abcba"), 4)

    def test_edge_case6(self):
        self.assertEqual(find_longest_repeating_subseq("ababab"), 4)

    def test_edge_case7(self):
        self.assertEqual(find_longest_repeating_subseq("abcabcabc"), 6)

    def test_edge_case8(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_edge_case9(self):
        self.assertEqual(find_longest_repeating_subseq("aabbcc"), 4)

    def test_edge_case10(self):
        self.assertEqual(find_longest_repeating_subseq("aabbccdd"), 4)

    def test_edge_case11(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_edge_case12(self):
        self.assertEqual(find_longest_repeating_subseq("ab"), 1)

    def test_edge_case13(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 0)

    def test_edge_case14(self):
        self.assertEqual(find_longest_repeating_subseq("abcd"), 0)

    def test_edge_case15(self):
        self.assertEqual(find_longest_repeating_subseq("abcabc"), 3)

    def test_edge_case16(self):
        self.assertEqual(find_longest_repeating_subseq("abab"), 2)

    def test_edge_case17(self):
        self.assertEqual(find_longest_repeating_subseq("ababab"), 4)

    def test_edge_case18(self):
        self.assertEqual(find_longest_repeating_subseq("abababab"), 4)

    def test_edge_case19(self):
        self.assertEqual(find_longest_repeating_subseq("ababababab"), 4)

    def test_edge_case20(self):
        self.assertEqual(find_longest_repeating_subseq("abababababab"), 4)
