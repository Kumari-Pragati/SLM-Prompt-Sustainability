import unittest
from mbpp_668_code import str
from six.moves.re import sub

from _668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(replace("aaa", "a"), "aaaa")
        self.assertEqual(replace("bbbb", "b"), "bbbbbbbb")
        self.assertEqual(replace("ccccc", "c"), "ccccccccc")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(replace("", "a"), "")
        self.assertEqual(replace("a", ""), "")
        self.assertEqual(replace("aa", "a"), "aa")
        self.assertEqual(replace("aaaa", "a"), "aaaaa")
        self.assertEqual(replace("aaaaa", "a"), "aaaaaa")

    def test_special_cases(self):
        self.assertEqual(replace("aaaAaa", "a"), "aaaAaaAaa")
        self.assertEqual(replace("aaAaa", "a"), "aaAaaa")
        self.assertEqual(replace("Aaa", "a"), "Aaa")
        self.assertEqual(replace("aa", "A"), "aa")
