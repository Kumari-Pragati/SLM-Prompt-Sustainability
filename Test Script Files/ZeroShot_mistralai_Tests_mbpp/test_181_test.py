import unittest
from mbpp_181_code import common_prefix_util, common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix_util(self):
        self.assertEqual(common_prefix_util("flower", "flow"), "fl")
        self.assertEqual(common_prefix_util("dog", "dino"), "")
        self.assertEqual(common_prefix_util("abcd", "ab"), "ab")
        self.assertEqual(common_prefix_util("abc", "abcd"), "")

    def test_common_prefix(self):
        self.assertEqual(common_prefix([ "flower", "flow", "flight" ], 3), "fl")
        self.assertEqual(common_prefix([ "dog", "dino", "dolphin" ], 3), "")
        self.assertEqual(common_prefix([ "abcd", "abc", "ab" ], 3), "ab")
        self.assertEqual(common_prefix([ "abc", "abcd", "ab" ], 3), "")
