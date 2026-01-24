import unittest
from mbpp_39_code import Counter
from heapq import heappush, heappop, heapify

class TestRearrangeString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(rearrange_string(""), "")

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(rearrange_string(char), char)

    def test_two_characters(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 != char2:
                    self.assertEqual(rearrange_string(char1 + char2), char2 + char1)

    def test_multiple_characters(self):
        for sequence in [
            "aaaabbbbcccc",
            "aabbccddeeffgghh",
            "zzyxwvutsrqponmlkjihgfedcba",
        ]:
            self.assertEqual(rearrange_string(sequence), sequence)

    def test_long_string(self):
        long_string = "a" * 1000 + "b" * 1000
        self.assertEqual(rearrange_string(long_string), long_string)

    def test_edge_cases(self):
        self.assertEqual(rearrange_string("a"), "a")
        self.assertEqual(rearrange_string("aa"), "aa")
        self.assertEqual(rearrange_string("aabb"), "abba")
        self.assertEqual(rearrange_string("aaabb"), "ababba")
        self.assertEqual(rearrange_string("aabbcc"), "acbacbc")
        self.assertEqual(rearrange_string("aaabbbccc"), "abacbcbc")
        self.assertEqual(rearrange_string("aabbccddeeffgghh"), "acbdeeffgghh")
        self.assertEqual(rearrange_string("zzyxwvutsrqponmlkjihgfedcba"), "abacadabacadabacadabac")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, rearange_string, 123)
        self.assertRaises(TypeError, rearange_string, [])
        self.assertRaises(TypeError, rearange_string, (1, 2, 3))
        self.assertRaises(TypeError, rearange_string, {"a": 1, "b": 2})
