import unittest
from mbpp_747_code import lcs_of_three

class TestLCSofThree(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(lcs_of_three("", "", "", 0, 0, 0), 0)

    def test_single_character_inputs(self):
        self.assertEqual(lcs_of_three("a", "a", "a", 1, 1, 1), 1)

    def test_short_strings(self):
        self.assertEqual(lcs_of_three("abc", "def", "ghi", 3, 3, 3), 0)

    def test_long_strings(self):
        self.assertEqual(lcs_of_three("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26, 26, 26), 26)

    def test_edge_cases(self):
        self.assertEqual(lcs_of_three("a", "b", "c", 1, 1, 1), 0)
        self.assertEqual(lcs_of_three("a", "a", "b", 1, 1, 1), 1)
        self.assertEqual(lcs_of_three("a", "a", "a", 1, 1, 1), 1)

    def test_lcs_of_three(self):
        self.assertEqual(lcs_of_three("abc", "def", "ghi", 3, 3, 3), 0)
