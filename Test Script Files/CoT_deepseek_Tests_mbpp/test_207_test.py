import unittest
from mbpp_207_code import find_longest_repeating_subseq

class TestFindLongestRepeatingSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_repeating_subseq("aabcb"), 2)

    def test_single_character(self):
        self.assertEqual(find_longest_repeating_subseq("a"), 1)

    def test_no_repeating_characters(self):
        self.assertEqual(find_longest_repeating_subseq("abc"), 1)

    def test_empty_string(self):
        self.assertEqual(find_longest_repeating_subseq(""), 0)

    def test_repeating_characters(self):
        self.assertEqual(find_longest_repeating_subseq("aabbcc"), 3)

    def test_long_string(self):
        self.assertEqual(find_longest_repeating_subseq("aabcb" * 1000), 2)

    def test_same_characters(self):
        self.assertEqual(find_longest_repeating_subseq("aaaaaa"), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_longest_repeating_subseq(123)
