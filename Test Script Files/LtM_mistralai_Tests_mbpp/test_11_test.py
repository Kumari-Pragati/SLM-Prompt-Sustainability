import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_simple_removal(self):
        self.assertEqual(remove_Occ("abc", "a"), "bc")
        self.assertEqual(remove_Occ("aaa", "a"), "")
        self.assertEqual(remove_Occ("abca", "a"), "bc")
        self.assertEqual(remove_Occ("abcab", "b"), "aac")

    def test_edge_cases(self):
        self.assertEqual(remove_Occ("", "a"), "")
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("aa", "b"), "aa")
        self.assertEqual(remove_Occ("ab", "b"), "a")

    def test_complex_scenarios(self):
        self.assertEqual(remove_Occ("aabbccaa", "a"), "bcc")
        self.assertEqual(remove_Occ("aaabbccaa", "b"), "aaacc")
        self.assertEqual(remove_Occ("aaaabbccaa", "c"), "aaabbaa")
