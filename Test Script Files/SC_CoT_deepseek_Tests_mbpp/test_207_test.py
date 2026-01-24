import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(find_longest_repeating_subseq("aabcb"), 2)

    def test_edge_case(self):
        self.assertEqual(find_longest_repeating_subseq("aaaaa"), 2)
        self.assertEqual(find_longest_repeating_subseq("abcde"), 1)

    def test_corner_case(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)
        self.assertEqual(find_longest_repeating_subseq("a"), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(12345)
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(None)
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(True)
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(["a", "b", "c"])
