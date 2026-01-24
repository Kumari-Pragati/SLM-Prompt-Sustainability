import unittest
from mbpp_39_code import rearange_string

class TestRearrangeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(rearange_string(char), char)

    def test_two_characters(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 != char2:
                    self.assertEqual(rearange_string(char1 + char2), char2 + char1)

    def test_longer_string(self):
        for sequence in [
            "aaabbbccc",
            "aaaabbbbbccc",
            "zzzzzzzzzzzzzz",
            "zzzzzzzzzzzzzzzz",
            "zzzzzzzzzzzzzzzzzz",
            "zzzzzzzzzzzzzzzzzzzz",
        ]:
            self.assertEqual(rearange_string(sequence), sequence)

    def test_edge_cases(self):
        self.assertEqual(rearange_string("a"), "a")
        self.assertEqual(rearange_string("aa"), "aa")
        self.assertEqual(rearange_string("aabb"), "abba")
        self.assertEqual(rearange_string("aabbcc"), "acbab")
        self.assertEqual(rearange_string("aabbccd"), "acbabd")
        self.assertEqual(rearange_string("aabbccdd"), "acbabcd")
        self.assertEqual(rearange_string("aabbccdde"), "acbabcdde")

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            rearange_string(123)
        with self.assertRaises(TypeError):
            rearange_string(None)
        with self.assertRaises(TypeError):
            rearange_string([])
